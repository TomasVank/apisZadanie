from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
CORS(app)
#run_with_ngrok(app)

@app.route('/', methods=['GET'])
def GetOrders():
  with open ('/content/OrderGetTable.ddl') as ddl_file:
    sql = ddl_file.read()
  myDb = MYSQL.connect(host="147.232.40.14", user="tv635vg", passwd="Airi8Eiw", database="tv635vg")
  cursor = myDb.cursor()
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  myDb.close()

  return jsonify(result),200

if __name__ == "__main__":
    app.run()
