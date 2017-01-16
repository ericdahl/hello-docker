FROM nginx:latest

RUN apt-get update && apt-get install -y --no-install-recommends curl unzip

ENV VERSION_CONSUL_TEMPLATE 0.16.0

RUN curl -SsL https://releases.hashicorp.com/consul-template/${VERSION_CONSUL_TEMPLATE}/consul-template_${VERSION_CONSUL_TEMPLATE}_linux_amd64.zip \
        | funzip - \
        > /usr/local/bin/consul-template \
    && chmod +x /usr/local/bin/consul-template


