from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"

@app.route("/hello/{name}")
def hello_world(name):
        return f"<p>Hello, {name}</p>"
