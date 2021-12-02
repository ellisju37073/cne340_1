#Justin Ellis
#CNE340 9/22/2021
#This will create a database and import data

import sqlite3

sqlite_file = "network.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS "
               "hosts(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "hostname TEXT, url TEXT, ip TEXT, local_or_remote TEXT, description TEXT)")
cursor.execute("INSERT INTO hosts(hostname, url, ip, local_or_remote, description)"
               "VALUES(?,?,?,?,?)", ("Localhost", "", "127.0.0.1","local","local host IP"))
connection.commit()
cursor.execute("SELECT hostname, url, ip, description  FROM hosts where local_or_remote = 'local'")

rows=cursor.fetchall()
print('Remote :')
for row in rows:
    print(row)

cursor.execute("SELECT hostname, url, ip, description  FROM hosts where local_or_remote = 'remote'")
rows=cursor.fetchall()
print('Remote :')
for row in rows:
    print(row)
connection.close()