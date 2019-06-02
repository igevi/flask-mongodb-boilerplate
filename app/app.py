import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['DEBUG'] = os.environ.get('ENV') == 'development'
app.config['PORT'] = os.environ.get('PORT')
db = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Welcome to Dockerized Flask with MongoDB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')