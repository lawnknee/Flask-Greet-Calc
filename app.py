from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Returns a simple "welcome" greeting"""

    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_welcome_home():
    """Returns a simple "welcome home" greeting"""

    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def say_welcome_back():
    """Returns a simple "welcome home" greeting"""

    html = "<html><body><h1>welcome back</h1></body></html>"
    return html
