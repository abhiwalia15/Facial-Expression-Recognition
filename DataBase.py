import sqlite3

con = sqlite3.connect('testfile.db')
print("OPENED")

table = "create table tab (song_names string, uri text, movies text)"

con.execute(table)
print("Table created")