import csv, sqlite3

sqlite_file = "Public_Computer_Access_Locations.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS locations(ID INTEGER PRIMARY KEY AUTOINCREMENT,'
               'Lab_name TEXT, Phone TEXT, Accessible TEXT, Hours TEXT , Tech_Support_Assisted TEXT, Organization TEXT,'
               ' Location TEXT, Web_address TEXT)')

with open(r'C:\Users\12069\Downloads\Public_Computer_Access_Locations_nocommas.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['Player'], i['Passing_Yds'], i['Yds_per_Attempt'], i['Attempt'], i['Cmp'], i['TD'],
              i['Interception']) for i in dr]

cursor.executemany("INSERT INTO quarterback(Player, Passing_Yds, Yds_per_Attempt, Attempt, Cmp, TD, Interception) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)

cursor.execute('SELECT Player, TD, Passing_Yds FROM quarterback WHERE TD > 6 ORDER BY TD')

rows = cursor.fetchall()
print('TD Leaders:')
for row in rows:
    print(row)
connection.commit()

