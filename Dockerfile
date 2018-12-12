FROM tiangolo/uwsgi-nginx-flask:python3.7

MAINTAINER Dave Hoffman

COPY ./app /app
RUN ls -alh /app
RUN pip3 install -r /app/requirements.txt
