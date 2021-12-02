import csv, sqlite3

sqlite_file = "Public_Computer_Access_Locations.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Public_Computer_Access_Locations(ID INTEGER PRIMARY KEY AUTOINCREMENT,'
               'Lab_name TEXT, Phone Integer, Accessible TEXT, Hours TEXT, Tech_Support_Assisted TEXT,'
               'Organization TEXT, Location TEXT, Web_address TEXT)')

with open(r'C:\Users\12069\Documents\CNA 330\Public_Computer_Access_Locations_nocommas.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Lab_name'], i['Phone'], i['Accessible'], i['Hours'], i['Tech_Support_Assisted'], ['Organization'],
              i['Location'], i['Web_address']) for i in dr]

cursor.executemany("INSERT INTO Public_Computer_Access_Locations (Lab_name, Phone, Accessible, Hours,"
                   "Tech_Support_Assisted, Organization, Location, Web_address)"
                    "VALUES (?,?,?,?,?,?,?,?);", to_db)

rows = cursor.fetchall()
print('Public_Computer_Access_Locations:')
for row in rows:
    print(row)
connection.commit()
connection.close()