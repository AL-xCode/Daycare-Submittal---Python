import sqlite3 as lite
import sys

con = lite.connect('textbooks.db')

with con:
    cur = con.cursor()
cur.execute("SELECT * FROM authors")

rows = cur.fetchall()

for row in rows:
    print(row)

# for row in cur.execute("SELECT * FROM authors"):
# print (row)

con.close()