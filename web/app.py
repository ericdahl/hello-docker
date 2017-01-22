import flask
import os
import redis
import consul
import socket

# FIXME: must be a better way
addr = socket.gethostbyname(socket.gethostname())

c = consul.Consul(host='consul')
ca = c.agent

check = consul.Check.http('http://' + addr + ':5000/health', '10s')
#FIXME: dynamic port
ca.service.register('web', address=addr, port=5000, service_id=os.environ['HOSTNAME'], check = check)


print(os.environ)



app = flask.Flask(__name__)


@app.route('/')
def hello_world():

    redis_handle = redis.StrictRedis(host='redis', port=6379, db=0)
    c = redis_handle.incr('counter')

    r = 'hello from {} (count is {})\n'.format(os.environ['HOSTNAME'], str(c))
    resp = flask.make_response(r)
    resp.headers['Cache-Control'] = 'public, max-age=5'
    return resp

@app.route('/health')
def health():
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
