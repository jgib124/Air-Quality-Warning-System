from flask import Flask, redirect, url_for

# Constructor Flask() takes the current module's name __name__ as argument
app = Flask(__name__)

# route() function is a decorator
# decorators used to modify the behavior of a function/class
# decorators take a function as the argument
# the @ symbol signifies a decorator
# route function is a decorator for the Flask class, tells the app which URL should call the function
# route(rule, options) where rule is the URL that is bind to the function
# options is a list of parameters that can be forwards to the rule object
@app.route('/')
def hello_world():
    return 'Hello World'

# Variables can be included in the URL routing using <>
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}"

# Variables can be ints, floats, or paths, but that must be specified within <>

@app.route('/numbers/evens/<int:num>')
def even_num(num):
    return f"This is even: {num}"

@app.route('/numbers/odds/<int:num>')
def odd_num(num):
    return f"This is odd: {num}"

@app.route('/numbers/<int:coolNum>')
def print_num(coolNum):
    if (coolNum % 2) == 0:
        return redirect(url_for('even_num', num=coolNum))
    else:
        return redirect(url_for('odd_num', num=coolNum))

# run() method runs the app on local development server
# run(host, port, debug, options)
# host: listens on host IP specified (defaults to local 127.0.0.1)
# port: port for IP, defaults to 5000 (127.0.0.1:5000)
# options: forwarded to Werkzeug server

if __name__ == '__main__':
    app.run(debug=True)
