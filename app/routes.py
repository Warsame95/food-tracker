from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/add')
def add():
    return render_template("add.html")