import sqlite3

# con = sqlite3.connect('testfile.db')
# print("OPENED")

# tables = "create table tab (song_names string, uri text, movies text)"

# print("Table created")

# tab = "insert into tab (song_names , uri , movies ) values ('bad lier', '1135g1g1fs1', 'project x')"
# con.execute(tab)

# **************************************************************
# *************************************************

# con = sqlite3.connect('test.db')
# c = con.cursor()

# c.execute("insert into list (songs, uri, movies) values(?,?,?)", ('asd','agh','aaa'))


# ******************************************************************8888
# ******************************************************



import sqlite3 
  
conn = sqlite3.connect('pythonDB.db') 
c = conn.cursor() 
  
def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)') 
  
def data_entry(): 
    number = 1234
    name = "GeeksforGeeks"
    c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name)) 
    conn.commit() 
  
create_table() 
data_entry() 
  
c.close() 
conn.close() 

# ********************************************************************
# **************************************************************


import sqlite3 
  
conn = sqlite3.connect('pythonDB.db') 
c = conn.cursor() 
  
def create_table(): 
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)') 
  
def data_entry(): 
    list = [1223, 'abhi'], [15, 'blon']
    print(list)
    for lists in list:
        print(lists)
        # c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", lists) 
        # conn.commit() 
  
create_table() 
data_entry() 
  
c.close() 
conn.close() 



# ********************************************************************
# **************************************************************

