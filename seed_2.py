import sqlite3
import fitz  # PyMuPDF
import re
import os

# === Setup Paths ===
db_path = "IAC-Bulletin.db"
pdf_path = "/Users/james/Downloads/BCP1928.pdf"

# === Delete old DB (if you want fresh imports each run) ===
if os.path.exists(db_path):
    os.remove(db_path)
    print("Existing database removed.")

# === Open PDF ===
doc = fitz.open(pdf_path)

# === Setup Database ===
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    season TEXT
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS collects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    type TEXT,
    reference TEXT,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)''')

# === Helper to extract reference from header lines ===
def extract_ref(line):
    match = re.search(r"[A-Za-z]+\.\s+[A-Za-z]+\s+[xiv]+\.*\s*\d*", line)
    return match.group(0).strip() if match else ""

# === Parse with a state machine ===
sunday_data = []
state = None
entry = {}

for page in doc:
    lines = page.get_text().split("\n")
    for raw_line in lines:
        line = raw_line.strip()

        # Title line
        if line.startswith("The") and "Sunday" in line:
            if entry:
                sunday_data.append(entry)
            entry = {
                "title": line.replace("The ", "").strip(),
                "collect": "",
                "epistle": "",
                "epistle_content": "",
                "gospel": "",
                "gospel_content": ""
            }
            state = None
            print(f"==> New entry: {entry['title']}")

        elif line.startswith("The Collect"):
            state = "collect"
            print("  -- Found Collect")

        elif line.startswith("The Epistle"):
            state = "epistle"
            entry["epistle"] = extract_ref(line)
            print(f"  -- Epistle: {entry['epistle']}")

        elif line.startswith("The Gospel"):
            state = "gospel"
            entry["gospel"] = extract_ref(line)
            print(f"  -- Gospel: {entry['gospel']}")

        else:
            if state == "collect":
                entry["collect"] += " " + line
            elif state == "epistle":
                entry["epistle_content"] += " " + line
            elif state == "gospel":
                entry["gospel_content"] += " " + line

# Save final entry
if entry:
    sunday_data.append(entry)

print(f"\nCollected {len(sunday_data)} Sundays.")

# === Insert into database ===
for entry in sunday_data:
    title = entry["title"]
    cur.execute("INSERT OR IGNORE INTO calendar (name, season) VALUES (?, ?)", (title, ""))
    cur.execute("SELECT id FROM calendar WHERE name = ?", (title,))
    cal_id_row = cur.fetchone()
    if not cal_id_row:
        print(f"Skipping: {title} (couldn't find calendar ID)")
        continue
    cal_id = cal_id_row[0]

    cur.execute("INSERT INTO collects (calendar_id, content) VALUES (?, ?)", (cal_id, entry["collect"].strip()))
    cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                (cal_id, "Epistle", entry["epistle"], entry["epistle_content"].strip()))
    cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                (cal_id, "Gospel", entry["gospel"], entry["gospel_content"].strip()))

conn.commit()
conn.close()
print("✅ All data committed to the database.")