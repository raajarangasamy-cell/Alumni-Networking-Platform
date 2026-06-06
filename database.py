import sqlite3

conn = sqlite3.connect("alumni.db")
print("Database Connected")
conn.close()
