from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_dir():
    return "<b>HELLO, WORLD!</b>"
