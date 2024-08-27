from flask import Flask, render_template
import pandas as pd

from dotenv import load_dotenv
load_dotenv()
print(load_dotenv())

server = Flask(__name__)

@server.route("/")
def base():
    return render_template("base.html")

@server.route("/blank")
def login():
    return "Hello, World2!"

@server.route("/example1")
def example1():
    df = pd.read_csv('./static/dataset/results.csv')
    data = df.head(10000)
    data = data.to_dict(orient='records')
    return render_template("example1.html", data_t=data)

@server.route("/example2")
def example2():
    df = pd.read_csv('./static/dataset/results.csv')
    data = df.head(10)
    return render_template("example2.html", data_t=data)