from flask import Flask
from time import ctime #ctime prints the current time as a string
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

#added this time web object that displays the current time
@app.route('/time')
def display_time():
    return ctime()


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
