from flask import Flask, render_template, request, redirect, url_for
from subprocess import call

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST','GET'])
def prediction():
    call(["python", "app.py"])
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)