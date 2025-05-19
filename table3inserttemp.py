import sqlite3

def insert_sunday(
    db_path,
    name,
    season,
    collect,
    first_lesson, first_ref,
    psalm, psalm_ref,
    second_lesson, second_ref,
    gospel, gospel_ref
):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Insert or find the calendar record
    cur.execute("INSERT OR IGNORE INTO calendar (name, season) VALUES (?, ?)", (name, season))
    cur.execute("SELECT id FROM calendar WHERE name = ?", (name,))
    result = cur.fetchone()
    if not result:
        raise Exception(f"Failed to retrieve calendar ID for {name}")
    calendar_id = result[0]

    # Insert readings (including Collect as a reading)
    readings = [
        ("Collect", None, collect),
        ("First Lesson", first_ref, first_lesson),
        ("Psalm", psalm_ref, psalm),
        ("Second Lesson", second_ref, second_lesson),
        ("Gospel", gospel_ref, gospel),
    ]

    for type_, ref, content in readings:
        cur.execute(
            "INSERT INTO readings (calendar_id, type, reference, content) VALUES (?, ?, ?, ?)",
            (calendar_id, type_, ref, content)
        )

    conn.commit()
    conn.close()