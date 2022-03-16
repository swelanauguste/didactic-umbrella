# pull official base image
FROM python:buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
COPY ./requirements/production.txt .
RUN pip install -r production.txt

# copy project
COPY . .