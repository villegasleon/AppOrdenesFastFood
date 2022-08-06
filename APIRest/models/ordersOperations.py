
from operator import concat
from models.databaseConnector import databaseConnector
from datetime import datetime
class ordersOperations:
    def get(status):
        try:
            conn = databaseConnector.get_db_connection()


            ordersIds = conn.execute('SELECT A.OrdersId FROM Orders A INNER JOIN StatusOrders B ON A.StatusOrdersId=B.StatusOrdersId WHERE B.name=?',(status,)).fetchall()
            ordersList = []

            for row in ordersIds:
                order = {}
                order['OrdersId'] = row['OrdersId']
                order['items'] = []

                productsOrder = conn.execute('SELECT C.Name AS ProductName, B.Amount FROM ProductsXOrders B INNER JOIN Products C ON B.ProductsID = C.ProductsID WHERE B.OrdersId=?',(row['OrdersId'],)).fetchall()

                for rowProductsOrder in productsOrder:
                    item = {}
                    item['ProductName'] = rowProductsOrder['ProductName']
                    item['Amount'] = rowProductsOrder['Amount']
                    
                    order['items'].append(item)

                ordersList.append(order)

            conn.close()
            return ordersList
        except Exception as exc:
            print(exc)

    def add(products):
        conn = databaseConnector.get_db_connection()
        productsTotal = {}

        for product in products:
            if product['sku'] in productsTotal:
                productsTotal[product['sku']] += product['amount']
            else:
                productsTotal[product['sku']] = product['amount']

        for product in productsTotal:
            rowProductsStock = conn.execute('SELECT Stock FROM Products WHERE sku=?',(product,)).fetchone()
            
            if rowProductsStock is None:
                return "The sku "+str(product)+" doesn't exist"

            productsStock= rowProductsStock["Stock"]

            if productsStock < productsTotal[product]:
                return "Error, there's no enough stock"

        rowStatusOrdersID = conn.execute('SELECT StatusOrdersID FROM StatusOrders WHERE Name= "Pending"').fetchone()
        statusOrdersID = rowStatusOrdersID['StatusOrdersID']

        createdDate = datetime.now()
        
        conn.execute('INSERT INTO Orders(CreatedDate, StatusOrdersID) VALUES (?,?)', (createdDate, statusOrdersID))
        
        conn.commit()

        rowOrdersID = conn.execute('SELECT MAX(OrdersID) AS OrdersID FROM Orders').fetchone()
        ordersID= rowOrdersID['OrdersID']

        for product in products:
            rowProductsID = conn.execute('SELECT productsID FROM Products WHERE sku = ?',(product['sku'],)).fetchone()
            productsID = rowProductsID['productsID']
            conn.execute('INSERT INTO ProductsXOrders(OrdersID,ProductsID, Amount) VALUES (?,?,?)', (ordersID,productsID,product['amount']))

        for product in productsTotal:
            rowProductsStock = conn.execute('UPDATE Products SET Stock = Stock - ? WHERE sku=?',(productsTotal[product],product,))

        conn.commit()

        conn.close()

        return "success"


    def update(status,ordersID):
        conn = databaseConnector.get_db_connection()
        rowStatusOrdersID = conn.execute('SELECT StatusOrdersID FROM StatusOrders WHERE Name= ?',(status,)).fetchone()
        statusOrdersID = rowStatusOrdersID['StatusOrdersID']

        conn.execute('UPDATE Orders SET StatusOrdersID=? WHERE OrdersID=?', (statusOrdersID, ordersID))
        conn.commit()
        conn.close()

    def delete(ordersID):
        conn = databaseConnector.get_db_connection()
        conn.execute('DELETE FROM Orders WHERE OrdersID=?', (ordersID,))
        conn.commit()
        conn.close()