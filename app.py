from flask import Flask, render_template, redirect
import requests
import time

app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template("index.html", data)

@app.route("/fit")
def fit():


if __name__ == "__main__":
    app.run(debug=True)
