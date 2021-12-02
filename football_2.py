import csv, sqlite3

sqlite_file = "quarterback.db"
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS quarterback(ID INTEGER PRIMARY KEY AUTOINCREMENT,'
               'Player TEXT, Passing_Yds Integer, Yds_per_Attempt REAL, Attempt INTEGER, Cmp INTEGER, TD INTEGER,'
               ' Interception INTEGER)')

with open(r'C:\Users\12069\Documents\CNA 330\football.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['Player'], i['Passing_Yds'], i['Yds_per_Attempt'], i['Attempt'], i['Cmp'], i['TD'],
              i['Interception']) for i in dr]

cursor.executemany("INSERT INTO quarterback (Player, Passing_Yds, Yds_per_Attempt, Attempt, Cmp, TD, Interception)"
                   "VALUES (?,?,?,?,?,?,?);", to_db)
cursor.execute('SELECT Player, TD, Passing_Yds from quarterback WHERE TD > 6 ORDER BY TD')

rows = cursor.fetchall()
print('TD Leaders:')
for row in rows:
    print(row)
connection.commit()
connection.close()