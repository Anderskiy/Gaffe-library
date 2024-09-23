from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)