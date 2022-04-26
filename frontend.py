from flask import Flask, redirect, url_for, request, render_template
import aqi

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
        return render_template('pollutants.html', name=user)
    else:
        user = request.args.get('usr')
        return render_template('pollutants.html', name=user)

'''
- render_template() function allows Jinja2 template to rend HTML files within python file

'''
@app.route('/pollutants/<name>', methods=['POST', 'GET'])
def table_inputs(name):
    if request.method == 'POST':
        ozone_input = request.form['oz']
        pm25_input = request.form['pm25']
        pm10_input = request.form['pm10']
        return redirect(url_for('generate_table', name=name, ozone_in=ozone_input,
                                pm25_in=pm25_input, pm10_in=pm10_input))
    else:
        ozone_input = request.args.get('oz')
        pm25_input = request.args.get('pm25')
        pm10_input = request.args.get('pm10')
        return redirect(url_for('generate_table', name=name, ozone_in=ozone_input,
                                pm25_in=pm25_input, pm10_in=pm10_input))

@app.route('/table/<name>_<float:ozone_in>_<float:pm25_in>_<float:pm10_in>')
def generate_table(name, ozone_in, pm25_in, pm10_in):
    o3_aqi_val = aqi.o3_aqi(ozone_in)

    return render_template('table.html', username = name, ozone = ozone_in,
                           o3_aqi = o3_aqi_val, pm25 = pm25_in, pm10 = pm10_in)

'''
- run() method runs the app on local development server
- run(host, port, debug, options)
- host: listens on host IP specified (defaults to local 127.0.0.1)
- port: port for IP, defaults to 5000 (127.0.0.1:5000)
- options: forwarded to Werkzeug server
'''
if __name__ == '__main__':
    app.run(debug=True)
