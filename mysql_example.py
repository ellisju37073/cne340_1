import mysql.connector
conn = mysql.connector.connect(user='root', password = '',
                               host='127.0.0.1',
                               database='cne340')
cursor=conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hosts(id INT PRIMARY KEY AUTO_INCREMENT,"
               "hostname TEXT, url TEXT, ip TEXT, local_or_remote TEXT, description TEXT)")
cursor.execute("INSERT INTO hosts(hostname, url, ip, local_or_remote, description)"
               "VALUES(%s,%s,%s,%s,%s)", ("Localhost", "", "127.0.0.1","local","local host IP"))
conn.commit()
cursor.execute("SELECT hostname, url, ip, description  FROM hosts where local_or_remote = 'local'")

rows=cursor.fetchall()
print('Local :')
for row in rows:
    print(row)

cursor.execute("SELECT hostname, url, ip, description  FROM hosts where local_or_remote = 'remote'")
rows=cursor.fetchall()
print('Remote :')
for row in rows:
    print(row)
conn.close()