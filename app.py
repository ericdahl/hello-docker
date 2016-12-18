from flask import Flask
import os


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Flask Dockerized. PORT is ' + os.environ['PORT'] + '\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)