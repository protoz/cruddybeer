FROM ubuntu

MAINTAINER Dave Hoffman

ENV NEW_NGINX_CONF_FILE=./config/nginx.conf \
    DEFAULT_NGINX_CONF_FILE=/etc/nginx/nginx.conf \
    NGINX_HTTP_PORT=80 \
    DOCKER_ENTRYPOINT=./config/docker-entrypoint.sh

RUN apt-get update \
    && apt-get install -y \
        nginx \
        sed

RUN rm -v ${DEFAULT_NGINX_CONF_FILE}

ADD ${NEW_NGINX_CONF_FILE} ${DEFAULT_NGINX_CONF_FILE}

COPY ${DOCKER_ENTRYPOINT} /etc/nginx/

#ENTRYPOINT ["/etc/nginx/docker-entrypoint.sh"]

RUN cat /etc/nginx/nginx.conf

EXPOSE ${NGINX_HTTP_PORT}

CMD nginx -g 'daemon off;'