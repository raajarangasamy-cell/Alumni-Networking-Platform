import sqlite3

conn = sqlite3.connect("alumni.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alumni (
    alumni_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    batch TEXT,
    company TEXT,
    designation TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    department TEXT,
    year INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    posted_by INTEGER
)
""")

conn.commit()
conn.close()

print("Database tables created successfully!")
