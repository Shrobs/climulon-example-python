#!/bin/bash

count=0
until ( python check_db.py )
do
  ((count++))
  if [ ${count} -gt 6 ]
  then
	echo "Postgres didn't become ready on time"
	exit 1
  fi
  sleep 5
done

python manage.py migrate

RUN_CMD="${@:-/usr/local/bin/gunicorn docker_django.wsgi:application -w 2 -b :8000}"

exec $RUN_CMD