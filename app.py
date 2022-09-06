from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href="https://jhaalbu-av-kllima-2-streamlit-app-9x0fnj.streamlitapp.com/">Klimascript er flytta hit</a>"
