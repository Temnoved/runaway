from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'MyName'
    return render_template('index.html', tname=name)
