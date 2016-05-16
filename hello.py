
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.google.com')     
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.setcookie('answer','42')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello , %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)

