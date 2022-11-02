from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="https://app-avtools-klima-dev.azurewebsites.net/">Klimascript er flytta hit</a>'
