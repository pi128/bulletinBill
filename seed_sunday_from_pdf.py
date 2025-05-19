import sqlite3
import fitz  # PyMuPDF
import re
import os

# File paths
db_path = "IAC-Bulletin.db"         # Update path if needed
pdf_path = "/Users/james/Downloads/BCP1928.pdf"          # Make sure this is local

# Open the PDF
doc = fitz.open(pdf_path)

if os.path.exists(db_path):
    os.remove(db_path)
    print("✅ Deleted existing database.")
    
# Open or create the database
conn = sqlite3.connect(db_path)
cur = conn.cursor()




# Create tables if they don't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    season TEXT
)
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS collects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    type TEXT,
    reference TEXT,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)
''')

# Helper to extract references like "Romans 13:8–14"
def extract_ref(block):
    lines = block.strip().split("\n") if block else []
    for line in lines:
        if re.search(r"[A-Za-z]+\s+\d+:\d+", line):
            return line.strip().rstrip(".")
    return ""

# Begin collecting Sundays after this marker
sunday_data = []
start_collecting = False

for page in doc:
    text = page.get_text()
    if "The First Sunday in Advent" in text:
        start_collecting = True
    if not start_collecting:
        continue

    matches = re.findall(
        r"(The (?:First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|Eleventh|Twelfth|Last).*?Sunday.*?)\n"
        r"(The Collect.*?)(?=\nThe Epistle|\nThe Gospel|\nThe .*?Sunday|\Z)"
        r"(The Epistle.*?)(?=\nThe Gospel|\nThe .*?Sunday|\Z)?"
        r"(The Gospel.*?)(?=\nThe .*?Sunday|\Z)?",
        text,
        re.DOTALL
    )

    for match in matches:
        title, _, collect_raw, epistle_raw, gospel_raw = match

        def label_block(block):
            lines = block.strip().split("\n") if block else []
            ref = ""
            content = []
            for line in lines:
                line = line.strip()
                if not ref and re.search(r"[A-Za-z]+\s+\d+[:.]\d+", line):
                    ref = line.rstrip(".")
                elif line:
                    content.append(line)
            return ref, " ".join(content)

        epistle_ref, epistle_content = label_block(epistle_raw) if epistle_raw else ("", "")
        gospel_ref, gospel_content = label_block(gospel_raw) if gospel_raw else ("", "")
        # Clean up the collect
        collect_lines = collect_raw.split("\n")[1:] if collect_raw else []
        collect_text = " ".join(line.strip() for line in collect_lines if line.strip())

        # Normalize and clean up the title
        clean_title = title.strip().replace("\n", " ")
        clean_title = re.sub(r"^The\s+", "", clean_title, flags=re.IGNORECASE)
        clean_title = re.sub(r"\s+", " ", clean_title)  # collapse multiple spaces

        clean_title = clean_title.strip()

        # Add one of the filters below depending on how strict you want it
        if "Collects, Epistles" in clean_title or not re.search(r"Sunday", clean_title):
            continue  # Skip intro or non-Sunday items

        # Skip titles that are actually the first line of a Gospel reading
        if clean_title.lower().startswith(("gospel", "epistle", "centurion", "jesus", "lord", "o lord")):
            continue
        sunday_data.append({
            "title": clean_title,
            "collect": collect_text,
            "epistle": epistle_ref,
            "epistle_content": epistle_content.strip(),
            "gospel": gospel_ref,
            "gospel_content": gospel_content.strip()
        })


# Insert into database
for entry in sunday_data:
    cur.execute("INSERT OR IGNORE INTO calendar (name, season) VALUES (?, ?)", (entry["title"], ""))
    cur.execute("SELECT id FROM calendar WHERE name = ?", (entry["title"],))
    row = cur.fetchone()
    if not row:
        print(f"Warning: calendar ID not found for {entry['title']}")
        continue
    cal_id = row[0]

    # Only insert collect if not already present
    cur.execute("SELECT 1 FROM collects WHERE calendar_id = ?", (cal_id,))
    if not cur.fetchone():
        cur.execute("INSERT INTO collects (calendar_id, content) VALUES (?, ?)", (cal_id, entry["collect"]))

    # Only insert epistle if not already present
    cur.execute("SELECT 1 FROM readings WHERE calendar_id = ? AND type = 'Epistle'", (cal_id,))
    if not cur.fetchone():
        cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                    (cal_id, "Epistle", entry["epistle"], entry["epistle_content"]))

    # Only insert gospel if not already present
    cur.execute("SELECT 1 FROM readings WHERE calendar_id = ? AND type = 'Gospel'", (cal_id,))
    if not cur.fetchone():
        cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                    (cal_id, "Gospel", entry["gospel"], entry["gospel_content"]))