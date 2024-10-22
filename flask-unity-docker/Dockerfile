FROM python:3.10.12-alpine

LABEL name="simple-flask-unity-app"
LABEL version="0.0.1"
LABEL description="A simple flask-unity application using docker"
MAINTAINER Usman Musa

RUN pip install --upgrade pip

RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./schoolsite /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
