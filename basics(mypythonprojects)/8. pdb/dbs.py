from sqlite3 import *
def setup():
    conn = connect("pydb.db")
    c = conn.cursor()

def insert(name, age, height, ethn):
    conn = connect("pydb.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO mytable VALUES('{name}', '{age}', '{height}', '{ethn}')")
    conn.commit()
    conn.close()

def query(searchby, search):
    conn = connect("pydb.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM mytable WHERE {searchby} LIKE '{search}%'")
    x = c.fetchall()
    conn.commit()
    conn.close()
    return x

def delete(id):
    conn = connect("pydb.db")
    c = conn.cursor()
    c.execute(f"DELETE * FROM mytable where rowid = {id}")
