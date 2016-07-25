FROM ubuntu

MAINTAINER Dave Hoffman

ENV GIT_BRANCH=development

#Install requirements like pip, flask, git and flask requirements
RUN apt-get update && apt-get install python-pip git
RUN pip install flask mongoengine
#Pull cruddybeer from git repo

#Run Cruddybeer in a way that Ngnix will accept - uWSGI probably.