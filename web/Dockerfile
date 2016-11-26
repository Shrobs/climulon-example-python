FROM python:3.5-onbuild

ADD entrypoint.sh /

ENTRYPOINT /entrypoint.sh

CMD /usr/local/bin/gunicorn docker_django.wsgi:application -w 2 -b :8000
