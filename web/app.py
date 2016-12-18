#from flask import Flask
import flask
import os


app = flask.Flask(__name__)
@app.route('/')
def hello_world():
    #r = 'Flask Dockerized. PORT is ' + os.environ['PORT'] + '\n'
    r = str(os.environ)
    r = 'Hello from ' + os.environ['HOSTNAME'] + '\n'
    resp = flask.Response(r)
    resp.headers['Cache-Control'] = 'public, max-age=5'
    return resp
    #return 'Flask Dockerized. PORT is ' + os.environ['PORT'] + '\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
