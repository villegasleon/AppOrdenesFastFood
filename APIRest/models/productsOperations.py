from math import prod
from models.databaseConnector import databaseConnector
import sqlite3
class productsOperations:
    def get():
        try:
            conn = databaseConnector.get_db_connection()
            products = conn.execute('SELECT productsId, name, description, stock,sku FROM products').fetchall()
            productsList = []

            for row in products:
                product ={}
                product['productsId'] = row['productsId']
                product['name'] = row['name']
                product['description'] = row['description']
                product['stock'] = row['stock']
                product['sku'] = row['sku']
                productsList.append(product)

            conn.close()
            return productsList
        except Exception as exc:
            print(exc)

    def add(name, description, stock, sku):
        conn = databaseConnector.get_db_connection()

        rowProductsID = conn.execute('SELECT ProductsID FROM Products WHERE sku=?',(sku,)).fetchone()

        #This code is validating if sku is duplicated or not, if not, the sku is added.        
        if rowProductsID is None:
            conn.execute('INSERT INTO products(name, description,stock,sku) VALUES (?,?,?,?)', (name, description,stock, sku))
            conn.commit()
            conn.close()

            return "success"
        else:
            return "sku is duplicated" 
        
    def update(name, description, stock, sku):
        conn = databaseConnector.get_db_connection()
        conn.execute('UPDATE products SET name=?, description=?, stock=? WHERE sku=?', (name, description,stock, sku))
        conn.commit()
        conn.close()

    def delete(sku):
        conn = databaseConnector.get_db_connection()
        conn.execute('DELETE FROM products WHERE sku=?', (sku,))
        conn.commit()
        conn.close()