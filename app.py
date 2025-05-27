from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'fmaybe Fully working, please and also sigfnefdfdfd ;)?'
