#!/bin/bash -x

set -o errexit

if [ -n "$WSGI_SERVER" ]; then
    sed 's/cruddybeer-app\:8001/$WSGI_SERVER' /etc/nginx/nginx.conf
fi
