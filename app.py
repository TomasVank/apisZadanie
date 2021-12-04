from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
#run_with_ngrok(app)

@app.route('/GetOrders', methods=['GET'])
def GetOrders():
  with open ('content/OrderGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()

  return jsonify(result),200

@app.route('/GetOrders/<id>', methods=['GET'])
def GetIdOrder(id):
  with open ('content/OrderByIdGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql+id)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/GetProducts', methods=['GET'])
def GetProducts():
  with open ('content/ProductGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/GetCustomers', methods=['GET'])
def GetCustomers():
  with open ('content/CustomerGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()
  return jsonify(result),200

@app.route('/CreateOrder', methods=["POST"])
def CreateOrder():
  data = request.get_json(force=True)
  order_dict = dict(data)
  with open ('content/OrderInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(order_dict["orders_ID"], order_dict["product_ID"],order_dict["customer_ID"],order_dict["orders_quantity"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201


@app.route('/CreateCustomer', methods=["POST"])
def CreateCustomer():
  data = request.get_json(force=True)
  customer_dict = dict(data)
  with open ('content/CustomerInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(customer_dict["customer_ID"], customer_dict["customer_firstName"],customer_dict["customer_lastName"],customer_dict["customer_phone"],customer_dict["customer_email"],customer_dict["customer_address"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201

@app.route('/CreateProduct', methods=["POST"])
def CreateProduct():
  data = request.get_json(force=True)
  product_dict = dict(data)
  with open ('content/ProductInsertTable.ddl') as ddl_file:
    sql = ddl_file.read()
    sql = sql[:-1] + "'{}','{}','{}','{}')"
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql.format(product_dict["product_ID"], product_dict["product_name"], product_dict["product_price"], product_dict["product_pieces_WH"]))
  myDb.commit()
  cursor.close()
  myDb.close()
  return jsonify("Created"),201


if __name__ == "__main__":
    app.run()
