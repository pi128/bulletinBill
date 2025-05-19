import sqlite3

conn = sqlite3.connect("IAC-Bulletin.db")
cur = conn.cursor()

# Create the tables
cur.execute("""
CREATE TABLE IF NOT EXISTS calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    season TEXT,
    liturgical_order INTEGER
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS collects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    calendar_id INTEGER,
    type TEXT,
    reference TEXT,
    content TEXT,
    FOREIGN KEY(calendar_id) REFERENCES calendar(id)
)
""")

conn.commit()
conn.close()