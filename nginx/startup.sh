#!/usr/bin/env sh

# FIXME: this is a horrible hack
sleep 10 
consul-template -consul consul:8500 -template "/etc/nginx/nginx.conf.ctmpl:/etc/nginx/nginx.conf" &

sleep 10
#consul-template -consul consul:8500 -template "/etc/nginx/nginx.conf.ctmpl" -dry &
#nohup consul-template -consul consul:8500 -template "/etc/nginx/nginx.conf.ctmpl" -dry &

#sleep 10 
nginx -g "daemon off;"

