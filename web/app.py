from flask import Flask
import os


app = Flask(__name__)
@app.route('/')
def hello_world():
    #r = 'Flask Dockerized. PORT is ' + os.environ['PORT'] + '\n'
    r = str(os.environ)
    r = 'Hello from ' + os.environ['HOSTNAME'] + '\n'
    #return 'Flask Dockerized. PORT is ' + os.environ['PORT'] + '\n'
    return r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
