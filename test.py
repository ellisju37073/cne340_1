#Rick Sturza
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
               "VALUES(?,?,?,?,?)", ("Ikea", "www.ikea.com", "193.182.147.214", "remote", "Online site to buy furniture"))
cursor.execute("INSERT INTO hosts(hostname, url, ip, local_or_remote, description)"
               "VALUES(?,?,?,?,?)", ("Discord", "www.Discord.com", "162.159.136.232", "remote", "Easiest way to talk over voice, video, and text"))
cursor.execute("INSERT INTO hosts(hostname, url, ip, local_or_remote, description)"
               "VALUES(?,?,?,?,?)", ("Addicting Games", "www.addictinggames.com", "104.22.3.109", "remote", "Free flash games online"))
cursor.execute("INSERT INTO hosts(hostname, url, ip, local_or_remote, description)"
               "VALUES(?,?,?,?,?)", ("Hulu", "www.Hulu.com", "208.91.158.0", "remote", "Online streaming of TV and movies"))