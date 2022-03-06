FROM python:3.8-slim-buster

RUN pip3 install flask

COPY . /app/

RUN chgrp -R 0 /app && chmod -R g=u /app 

WORKDIR /app

EXPOSE 8000
CMD ["/bin/sh", "start.sh"]
