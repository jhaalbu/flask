from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="https://av-klima.streamlitapp.com/">Klimascript er flytta hit</a>'
