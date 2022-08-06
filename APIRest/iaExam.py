from flask import Flask, jsonify, request
from models.ordersOperations import ordersOperations
from models.productsOperations import productsOperations
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/products", methods=['POST', 'GET'], defaults={'sku':None})
@app.route("/products/<int:sku>", methods=['PUT', 'DELETE'])
def products(sku):
    try:
        if request.method=='GET':
            try:
                products= productsOperations.get()
                print(products)
                data = {"status": "success", "data":products}
                return data, 200
            except Exception as err:
                print(err)

        elif request.method=='POST':
            try:
                request_data = request.get_json() 

                result= productsOperations.add(request_data['name'],request_data['description'],request_data['stock'],request_data['sku'])
                if result =="success":
                    
                    data = {"status": "success"}
                    return data, 200

                else:
                    data = {"message": result}
                    return data, 400
                    
            except Exception as err:
                print(err)

        elif request.method=='PUT':
            try:
                request_data = request.get_json() 

                productsOperations.update(request_data['name'],request_data['description'],request_data['stock'],sku)
                data = {"status": "success"}
                return data, 200
            except Exception as err:
                print(err)

            
        elif request.method=='DELETE':
            try:
                productsOperations.delete(sku)
                data = {"status": "success"}
                return data, 200
            except Exception as err:
                print(err)


    except Exception as exc:
        print(exc)

@app.route("/orders", methods=['POST', 'GET'], defaults={'ordersId':None})
@app.route("/orders/<int:ordersId>", methods=['PUT', 'DELETE'])
def orders(ordersId):
    try:
        if request.method=='GET':
            try:
                status = request.args.get('status')
                print(status)
                orders= ordersOperations.get(status)
                data = {"status": "success", "data":orders}
                return data, 200
            except Exception as err:
                print(err)

        elif request.method=='POST':
            try:
                request_data = request.get_json() 
                result = ordersOperations.add(request_data['products'])

                if result =="success":
                    
                    data = {"status": "success"}
                    return data, 200

                else:
                    data = {"message": result}
                    return data, 400
            except Exception as err:
                print(err)    
                traceback.print_exc()


        elif request.method=='PUT':
            try:
                request_data = request.get_json() 
                ordersOperations.update(request_data['status'],ordersId)
                data = {"status": "success"}
                return data, 200

            except Exception as err:
                print(err)

            
        elif request.method=='DELETE':
            try:
                data = {"status": "success"}
                ordersOperations.delete(ordersId)
                return data, 200
            except Exception as err:
                print(err)


    except Exception as exc:
        print(exc)
