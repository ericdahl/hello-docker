Example showing the use of `consul-template` to dynamically update nginx load balancer pool with `docker-compose`

# Getting started

```bash
$ git clone https://github.com/ericdahl/hello-docker-consul-template.git

$ cd hello-docker-consul-template

$ docker-compose up

$ curl http://localhost

$ docker-compose scale web=3

# check current config
$ docker-compose exec nginx cat /etc/nginx/nginx.conf
```
