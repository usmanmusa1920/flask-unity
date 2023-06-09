FROM python:3.8.5-alpine

LABEL name="sakyum"
LABEL version="0.0.1"
LABEL description="A demo of sakyum website on docker"
MAINTAINER Usman Musa

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./schoolsite /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
