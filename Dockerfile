FROM python:3.6-alpine
#RUN apk add --update python py-pip mysql-dev build-base python-dev && rm -rf /var/cache/apk/*

# create a virtual environment and install all dependencies from pypi
RUN mkdir -p /golinks/app
WORKDIR /golinks

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app app
COPY migrations migrations
COPY manage.py config.py entrypoint.sh ./
RUN chmod +x entrypoint.sh

ENV FLASK_APP manage.py
ENV FLASK_CONFIG production

# expose port(s)
EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
