from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"

@app.route('/post')
def greeting():
        return "<p>Hello, post!</p>"

@app.route('/hello/<name>')
def hello(name='world'):
    return f'Hello, {name}!'
