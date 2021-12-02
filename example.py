import csv, sqlite3

with open(r'C:\Users\12069\Documents\CNA 330\Public_Computer_Access_Locations.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['Lab_name'], i['Phone'], i['Accessible'], i['Hours'], i['Tech_Support_Assisted'], i['Organization'],
              i['Location'], i ['Web_address']) for i in dr]
   