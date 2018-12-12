FROM tiangolo/uwsgi-nginx-flask:python3.7

MAINTAINER Dave Hoffman

RUN rm -rf /app

ADD . /app

RUN pip3 install -r /app/requirements.txt
