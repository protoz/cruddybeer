FROM ubuntu

MAINTAINER Dave Hoffman

ENV GIT_BRANCH=dockerize

#Install requirements like pip, flask, git and flask requirements
RUN apt-get update \
    && apt-get install \
        python3-pip \
        wget \
        unzip \
        -y
RUN pip3 install \
    uwsgi \
    flask \
    flask-mongoengine
    
#Pull cruddybeer from git repo
RUN wget https://github.com/protoz/cruddybeer/archive/${GIT_BRANCH}.zip \
    && unzip ${GIT_BRANCH}.zip \
    && mv cruddybeer-${GIT_BRANCH} env

#Run Cruddybeer in a way that Ngnix will accept - uWSGI probably.
CMD uwsgi --ini /env/uwsgi.ini