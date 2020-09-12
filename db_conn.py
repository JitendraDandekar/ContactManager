import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contacts(id integer primary key autoincrement, fname text, lname text, mob integer, email text)")
        self.conn.commit()

    def insert(self, entities):
        self.cur.execute("INSERT INTO contacts(fname,lname,mob,email) VALUES(?,?,?,?)", entities)
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT fname,lname,mob,email FROM contacts order by fname")
        data = self.cur.fetchall()
        return data

    def match(self):
        self.cur.execute("SELECT * FROM contacts order by fname")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM contacts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, fname, lname, mob, email, id):
        self.cur.execute("UPDATE contacts SET fname=?, lname=?, mob=?, email=? where id=?", (fname, lname, mob, email, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
