from flask import Flask, redirect, url_for, request, render_template

# Constructor Flask() takes the current module's name __name__ as argument
app = Flask(__name__)

'''
- route() function is a decorator
- decorators used to modify the behavior of a function/class
- decorators take a function as the argument
- the @ symbol signifies a decorator
- route function is a decorator for the Flask class, tells the app which URL should call the function
- route(rule, options) where rule is the URL that is bind to the function
- options is a list of parameters that can be forwards to the rule object
'''
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


'''
- url_for() function accepts the name of another function as parameter
- accepts keyword arguments as variables for url
'''
@app.route('/numbers/<int:coolNum>')
def print_num(coolNum):
    if (coolNum % 2) == 0:
        return redirect(url_for('even_num', num=coolNum))
    else:
        return redirect(url_for('odd_num', num=coolNum))

'''
- HTTP methods (GET, POST, etc.) can be specified in route()
- In HTML file, url at /login is mapped to this function
- form is POSTed to this URL in the action tag of the form clause
- POST sends HTML form data to server
- 'nm' is variable name specified in HTML file
- method can be changed between GET and POST in the HTML file
'''

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['usr']
        return redirect(url_for('generate_table', name=user))
    else:
        user = request.args.get('usr')
        return redirect(url_for('generate_table', name=user))

'''
- render_template() function allows Jinja2 template to rend HTML files within python file

'''
@app.route('/pollutants/<name>', methods=['POST', 'GET'])
def generate_table(name):
    if request.method == 'POST':
        ozone_input = request.form['oz']
        pm25_input = request.form['pm25']
        pm10_input = request.form['pm10']
        return render_template('table.html', template_folder='html', username=name, ozone=ozone_input,
                               pm25=pm25_input, pm10=pm10_input)
    else:
        ozone_input = request.args.get('oz')
        pm25_input = request.args.get('pm25')
        pm10_input = request.args.get('pm10')
        return render_template('table.html', template_folder='html', username=name, ozone=ozone_input,
                               pm25=pm25_input, pm10=pm10_input)





'''
- run() method runs the app on local development server
- run(host, port, debug, options)
- host: listens on host IP specified (defaults to local 127.0.0.1)
- port: port for IP, defaults to 5000 (127.0.0.1:5000)
- options: forwarded to Werkzeug server
'''
if __name__ == '__main__':
    app.run(debug=True)
