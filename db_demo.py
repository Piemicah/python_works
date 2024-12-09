import sqlite3


conn = sqlite3.connect("colors.db")

cur = conn.cursor()

cur.execute("select * from kolors where colorname=?", ("Brass",))

result = cur.fetchone()

print(result)
