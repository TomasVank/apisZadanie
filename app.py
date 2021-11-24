from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL


app = Flask(__name__)
CORS(app)

ovocie = ["jablko","pomaranc","jahoda"]

@app.route("/", methods=["GET"])
def main():
    return jsonify({"ovocie":ovocie}),200

@app.route("/vytvorit", methods=["POST"])
def create():
    data = request.get_json(force=True)
    data_dict = dict(data)
    ovocie.append(data_dict["vytvorit"])
    return jsonify("created"),201

@app.route("/upravit/<id>", methods=["PUT"])
def update(id):
    data = request.get_json(force=True)
    data_dict = dict(data)
    ovocie[int(id)] = data_dict["upravit"]
    return jsonify("updated"),201

@app.route("/vymazat/<id>", methods=["DELETE"])
def delete(id):
    del ovocie[int(id)]
    return jsonify("deleted"),204

if __name__ == "__main__":
    app.run()
