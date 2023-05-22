#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:p>')
def print_string(p):
    print(p)
    return f'{p}'

@app.route('/count/<int:num>')
def count(num):
    count = f''
    for i in range(num):
        count += f'{i}\n'
    return count
    
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    else:
        print("That is not a valid operation.")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
