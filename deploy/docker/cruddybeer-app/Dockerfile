FROM ubuntu

MAINTAINER Dave Hoffman

ENV GIT_BRANCH=development

#Install requirements like pip, flask, git and flask requirements
RUN apt-get update \
    && apt-get install python3-pip wget unzip -y
RUN pip3 install uwsgi flask flask-mongoengine
#Pull cruddybeer from git repo
RUN wget https://github.com/protoz/cruddybeer/archive/${GIT_BRANCH}.zip && unzip ${GIT_BRANCH}.zip
RUN ls -alh /cruddybeer-${GIT_BRANCH}
#Run Cruddybeer in a way that Ngnix will accept - uWSGI probably.
CMD uwsgi -s /tmp/uwsgi.sock --protocol=http --manage-script-name --mount /cruddybeer-${GIT_BRANCH}/=run.py