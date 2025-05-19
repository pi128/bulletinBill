import requests
from bs4 import BeautifulSoup
import sqlite3

# Base URL and calendar pages to scrape
base_url = "http://justus.anglican.org/resources/bcp/1928/"
calendar = {
    "First Sunday in Advent": "collects/adv1.htm",
    "Second Sunday in Advent": "collects/adv2.htm",
    # Add more entries here
}

conn = sqlite3.connect("IAC-Bulletin.db")
cur = conn.cursor()

# Ensure required tables exist
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

for name, path in calendar.items():
    url = base_url + path
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Extract and clean the full text
    paragraphs = soup.find_all("p")
    full_text = "\n".join(p.get_text() for p in paragraphs).strip()

    # Extract collect (before "The Epistle")
    if "The Epistle" in full_text:
        collect = full_text.split("The Epistle")[0].strip()
    else:
        collect = ""

    # Extract epistle
    epistle_ref = ""
    gospel_ref = ""
    if "The Epistle" in full_text:
        epistle_section = full_text.split("The Epistle")[1]
        if "The Gospel" in epistle_section:
            epistle_ref = epistle_section.split("The Gospel")[0].strip().split("\n")[0]
        else:
            epistle_ref = epistle_section.strip().split("\n")[0]

    # Extract gospel
    if "The Gospel" in full_text:
        gospel_section = full_text.split("The Gospel")[1]
        gospel_ref = gospel_section.strip().split("\n")[0]

    # Insert calendar entry
    cur.execute("INSERT OR IGNORE INTO calendar (name, season) VALUES (?, ?)", (name, "Advent"))
    cal_id = cur.lastrowid
    cur.execute("SELECT id FROM calendar WHERE name = ?", (name,))
    cal_id = cur.fetchone()[0]

    # Insert collect
    cur.execute("INSERT INTO collects (calendar_id, content) VALUES (?, ?)", (cal_id, collect))

    # Insert readings
    cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                (cal_id, "Epistle", epistle_ref, ""))
    cur.execute("INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
                (cal_id, "Gospel", gospel_ref, ""))

cur.execute("SELECT name FROM calendar;")
print(cur.fetchall())

conn.commit()
conn.close()

