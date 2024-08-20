from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

def datetimeformat(value):
    value = int(value)
    return datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def datetimeformat13(value):
    value = int(value)
    return datetime.fromtimestamp(value/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['datetimeformat13'] = datetimeformat13

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    token = request.args.get('token')
    netid = request.args.get('netid')
    fcdt = request.args.get('fcdt')
    tcdt = request.args.get('tcdt')
    url = f"https://app.alphax.cloud/getPathData?token={token}&netid={netid}&fcdt={fcdt}&tcdt={tcdt}"
    print(url)
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
