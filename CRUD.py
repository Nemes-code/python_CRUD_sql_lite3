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
self.con.commit()


#INSERT FUNCTION

def insert(self, name, age):
    self.cur.execute("insert into employees values (NULL,?,?)", (name,age))
    self.con.commit()

#FETCH ALL DATA FORM DB
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows
    
#DELETE RECORD IN DB
    def remove(self,id,):
        self.cur.execute("dlete from employees where id=?",(id,))
        self.con.commit()

#UPDATE RECORD IN DB
        def update(self,id, name, age):
            self.cur.execute("update employees set name=?, age=? where id=?",
                             (name,age,id))
            self.con.commit()

            O=Database("Employee.db")
    