from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Anonymous')
    message = request.form.get('message', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('result.html', name=name, message=message, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True) 