import sqlite3

#CREATING A TABLE
class Database:

    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
CREATE TABLE IF NOT EXISTS employees(
id integer Primary Key, name text, age text
)
"""
self.cur.execute(sql)
slef.con.commit()