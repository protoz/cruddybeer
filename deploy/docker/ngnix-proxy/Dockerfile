FROM ubuntu

MAINTAINER Dave Hoffman

ENV NEW_NGNIX_CONF_FILE=config/ngnix.conf \
    OLD_NGNIX_CONF_FILE=/etc/ngnix/ngnix.conf \
    NGNIX_HTTP_PORT=80

RUN apt-get update && apt-get install -y nginx

#Guides say to remove this file but it doesn't seem to exist in Xenial.  Need to troubleshoot further.
#RUN rm -v ${OLD_NGNIX_CONF_FILE}

ADD ${NEW_NGNIX_CONF_FILE} ${OLD_NGNIX_CONF_FILE}

EXPOSE ${NGNIX_HTTP_PORT}

CMD service ngnix start