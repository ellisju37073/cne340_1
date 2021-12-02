#Justin Ellis
#CNE340 9/22/2021
#This will create a database and import data

import sqlite3

sqlite_file = "superheroes.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS "
               "Heroes(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name TEXT, universe TEXT, grade REAL)")
cursor.execute("INSERT INTO Heroes(name, universe, grade)"
               "VALUES(?,?,?)", ("Batman", "DC", 10.00))
cursor.execute("INSERT INTO Heroes(name, universe, grade)"
               "VALUES(?,?,?)", ("Wonder Woman", "DC", 10.00))
cursor.execute("INSERT INTO Heroes(name, universe, grade)"
               "VALUES(?,?,?)", ("Superman", "DC", 9.8))
cursor.execute("INSERT INTO Heroes(name, universe, grade)"
               "VALUES(?,?,?)", ("Spiderman", "Marvel", 10.00))
cursor.execute("INSERT INTO Heroes(name, universe, grade)"
               "VALUES(?,?,?)", ("Wolverine", "Marvel", 10.00))
connection.commit()
cursor.execute("SELECT name FROM Heroes where universe = 'DC'")

rows=cursor.fetchall()
print('DC Super Heroes:')
for row in rows:
    print(row)
connection.close()