import sqlite3
import os.path

class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.con = self._connect_db()
        self.cur = self.con.cursor()

    def _connect_db(self):
        if os.path.exists(self.db_name):
            return sqlite3.connect(self.db_name)
        else:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
            )
            return con

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES(?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id = ?;", (prod_id,))
        self.con.commit()

    def get_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()
