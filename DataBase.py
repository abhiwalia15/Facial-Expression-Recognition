import sqlite3

# con = sqlite3.connect('testfile.db')
# print("OPENED")

# tables = "create table tab (song_names string, uri text, movies text)"

# print("Table created")

# tab = "insert into tab (song_names , uri , movies ) values ('bad lier', '1135g1g1fs1', 'project x')"
# con.execute(tab)


con = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("insert into list (songs, uri, movies) values('abc', 'asd', 'adfg')")
