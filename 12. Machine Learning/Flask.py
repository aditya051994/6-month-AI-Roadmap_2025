from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/index")
def Index():
    return "<p>Good Morning</P>"


app.run(host='127.0.0.1',port=5000)