from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/updates/')
def updates():
    return render_template('updates.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/help/')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)