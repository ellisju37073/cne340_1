import sqlite3
import json
import requests
import time


def connect_to_sql():
    sqlite_file = "fantasy.db"
    conn = sqlite3.connect(sqlite_file)

    return conn
def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS fantasy (id INTEGER PRIMARY KEY AUTOINCREMENT,playername TEXT, position TEXT, points INTEGER ); ''')
    return
def query_sql(cursor, query):
    cursor.execute(query)
    return cursor
def add_new_player(cursor, playerdetails):
    # extract all required columns
    Name = playerdetails['player_name']
    position = playerdetails['position']
    points = playerdetails["fantasy_points"]["ppr"]
    query = cursor.execute("INSERT INTO fantasy( playername, position, points" ") "
               "VALUES(?,?,?)", (Name, position, points))
    # https://stackoverflow.com/questions/20818155/not-all-parameters-were-used-in-the-sql-statement-python-mysql/20818201#20818201
    return query_sql(cursor, query)
def check_if_player_exists(cursor, playerdetails):
    playername = playerdetails['player_name']
    query = "SELECT * FROM fantasy WHERE playername = \"%s\"" % playername
    return query_sql(cursor, query)
def delete_player(cursor, playerdetails):
    playername = playerdetails['player_name']
    query = "DELETE FROM fantasy WHERE playername = \"%s\"" % playername
    return query_sql(cursor, query)
def fetch_new_players():

    query = requests.get("https://www.fantasyfootballdatapros.com/api/players/2019/1")
    datas = json.loads(query.text)

    return datas
def playerhunt( cursor):
    playerpage = fetch_new_players()
    add_or_delete_player( playerpage, cursor)
def add_or_delete_player( playerpage, cursor):
    # Add your code here to parse the job page
    for playerdetails in  playerpage:  # EXTRACTS EACH Player from list
        # Add in your code here to check if the player already exists in the DB
        check_if_player_exists(cursor, playerdetails)
        is_player_found = len(cursor.fetchall()) > 0  # https://stackoverflow.com/questions/2511679/python-number-of-rows-affected-by-cursor-executeselect
        if is_player_found:
            print("player is found: "+ playerdetails["player_name"] + " from " + playerdetails["team"])
        else:
            print("New player is found: " + playerdetails["player_name"] + " from " + playerdetails["team"])
            add_new_player(cursor, playerdetails)
def main():
    # Important, rest are supporting functions
    # Connect to SQL and get cursor
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_tables(cursor)
    # Load text file and store arguments into dictionary

    while(1):  # Infinite Loops. Only way to kill it is to crash or manually crash it. We did this as a background process/passive scraper
        playerhunt( cursor)  # arg_dict is argument dictionary,
        time.sleep(3600)  # Sleep for 1h, this is ran every hour because API or web interfaces have request limits. Your reqest will get blocked.
# Sleep does a rough cycle count, system is not entirely accurate
# If you want to test if script works change time.sleep() to 10 seconds and delete your table in MySQL
if __name__ == '__main__':
    main()