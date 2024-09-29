from flask import Flask, render_template, abort, session, redirect, url_for, request, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

token = '7890920959:AAHf4p2q5gk6mRY5LJIBKhznZvAqmaVETMs'
chat_id = '-1002328132480'


def send_message_to_telegram(subject, message):
    text = f'Нову повідомлення з сайту!\nТема: {subject}\nСообщение: {message}'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}

    response = requests.post(url, data=data)
    print(response.text)
    print(response.status_code == 200)
    return response.status_code == 200

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

@app.route('/films/<film_name>/')
def film(film_name):
    film_path = os.path.join(os.getcwd(), 'templates', 'films', film_name)

    if os.path.isdir(film_path):
        language = session.get('language', 'ua')
        if language == 'uk':
            return render_template(f'films/{film_name}/{film_name}_uk.html')
        else:
            return render_template(f'films/{film_name}/{film_name}_ua.html')
    else:
        abort(404)


@app.route('/submit_help', methods=['POST'])
def submit_help():
    subject = request.form.get('subject')
    message = request.form.get('message')

    send_message_to_telegram(subject, message)
    return None


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)