from flask import Flask, render_template, abort, session, redirect, url_for, request
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Головна сторінка
@app.route('/')
def index():
    language = session.get('language', 'ua')
    if language == 'uk':
        return render_template('index_uk.html')
    else:
        return render_template('index_ua.html')

# Маршрут для зміни мови
@app.route('/set_language/<lang>')
def set_language(lang):
    session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/about/')
def about():
    language = session.get('language', 'ua')
    if language == 'uk':
        return render_template('about_uk.html')
    else:
        return render_template('about_ua.html')

@app.route('/updates/')
def updates():
    language = session.get('language', 'ua')
    if language == 'uk':
        return render_template('updates_uk.html')
    else:
        return render_template('updates_ua.html')

@app.route('/resources/')
def resources():
    language = session.get('language', 'ua')
    if language == 'uk':
        return render_template('resources_uk.html')
    else:
        return render_template('resources_ua.html')

@app.route('/help/')
def help_page():
    language = session.get('language', 'ua')
    if language == 'uk':
        return render_template('help_uk.html')
    else:
        return render_template('help_ua.html')


if __name__ == '__main__':
    app.run(debug=True)