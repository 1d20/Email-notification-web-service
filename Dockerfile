FROM ubuntu:16.04

MAINTAINER 1d20

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	python3 python3-dev python3-setuptools python3-pip \
	git \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
	pip3 install uwsgi && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN mkdir /code/be
WORKDIR /code/be

ADD ./requirements.txt /code/be/
RUN pip install -r requirements.txt

COPY . /code/be/
RUN python /code/be/manage.py makemigrations
RUN python /code/be/manage.py migrate
