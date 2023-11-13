from flask import Flask, render_template, url_for, request
import requests

index = Flask(__name__)

@index.route('/', methods=['GET','POST'])
def home():
    return render_template("index.html")

@index.route('/weather', methods=['GET','POST'])
def weather():
    if request.method == 'POST':

        user_input = request.form['city']
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID=8987e057165d2a4223dd4d8308a2ddb1")
        if weather_data.json() ['cod'] == '404':
            return render_template('weather_notdisplayed.html')
        else:
            return render_template('weather_displayed.html', values=weather_data.json())
    else:
        return render_template('weather.html')

@index.route('/health', methods=['GET','POST'])
def health():
    return render_template('health.html')

@index.route('/consultation', methods=['GET','POST'])
def consultation():
    return render_template('consultation.html')

@index.route('/blog', methods=['GET','POST'])
def blog():
    return render_template('blog.html')

