from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

APP_VERSION = "1.0.1"  # Change this during demo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'Anonymous')
    message = request.form.get('message', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('result.html', name=name, message=message, timestamp=timestamp)

@app.route('/version')
def version():
    return f"<h1>Application Version: {APP_VERSION}</h1><p>Updated during live demo!</p>"

if __name__ == '__main__':
    app.run(debug=True) 