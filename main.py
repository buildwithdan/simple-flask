from flask import Flask

from dotenv import load_dotenv
load_dotenv()
print(load_dotenv())

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello, World!"

@server.route("/blank")
def test():
    return "Hello, World2!"