import sqlite3




class Database:

    def __init__(self, db, tb):
        self.tb = tb

        self.conn = sqlite3.connect(db)

        self.cur = self.conn.cursor()

        s = '''CREATE TABLE IF NOT EXISTS {}


                         (ID INT    PRIMARY KEY     NOT NULL,
                         NAME               TEXT    NOT NULL,
                         ADDRESS        CHAR(50),
                         TYPE           CHAR(50),
                         COORDINATES1    CHAR(50),
                         COORDINATES2    CHAR(50),
                         IMAM_NAME      CHAR(50));'''.format(tb)

        self.cur.execute(s)

        self.conn.commit()

    def insert(self, id, name, address, Mosque_Type, coordinates1, coordinates2, imam_name):
        self.cur.execute(
            "INSERT or IGNORE INTO {} (ID,NAME, ADDRESS, TYPE, COORDINATES1,COORDINATES2, IMAM_NAME) VALUES(?, ?, ?, ?, ?, ?, ?)".format(
                self.tb), (id, name, address, Mosque_Type, coordinates1, coordinates2, imam_name))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute(f"DELETE FROM {self.tb} WHERE ID = {id}")
        self.conn.commit()

    def update(self, id, name_edited):
        self.cur.execute(f"UPDATE {self.tb} SET IMAM_NAME = \"{name_edited}\" WHERE ID = {id}")
        self.conn.commit()

    def dispaly_all(self, The_table):
        self.cur.execute("SELECT * FROM {}".format(The_table))
        data = self.cur.fetchall()
        return data
