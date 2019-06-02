# flask-mongodb-boilerplate

## About

This is a simple boilerplate for a Dockerized Flask app with MongoDB to speed up the first stages of a new project using this stack. 
The boilerplate will start a Docker container for the Flask app and a separate Docker container for the MongoDB instance.

## Usage

This requires *Docker* and *Docker Compose* to be installed. Links to install guides for these will be added soon.

Firstly, clone the repository:

`$ git clone https://github.com/igevi/flask-mongodb-boilerplate`

The initial boilerplate app can then be started with

`$ docker-compose up --build`

By default this will be running on `localhost:5000`
