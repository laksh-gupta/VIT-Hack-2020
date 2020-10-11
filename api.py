from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_pymongo import PyMongo
import pymongo
import vithack_final

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'pymdb'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/pymdb'

mongo = PyMongo(app)

@app.route("/")
def Welcome():
    message = "Welcome, This is the IPL chatbot."
    render_template("welcome", message = message)


@app.route("/interact")
def interact():
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5000, debug = True)