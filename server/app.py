#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    numbers = [str(i) for i in range(num)]
    return '\n'.join(numbers)

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return 'Error: Modulo by zero!'
    else:
        return 'Error: Invalid operation!'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
