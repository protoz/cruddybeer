FROM ubuntu

MAINTAINER Dave Hoffman

ENV NEW_NGINX_CONF_FILE=./config/nginx.conf \
    OLD_NGINX_CONF_FILE=/etc/nginx/nginx.conf \
    NGINX_HTTP_PORT=80:80

RUN apt-get update \
    && apt-get install -y \
        nginx

RUN rm -v ${OLD_NGINX_CONF_FILE}

ADD ${NEW_NGINX_CONF_FILE} ${OLD_NGINX_CONF_FILE}

EXPOSE ${NGINX_HTTP_PORT}

CMD service nginx start