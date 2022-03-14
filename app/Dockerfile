# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
COPY ./requirements/production.txt .
COPY ./requirements/development.txt .
RUN pip install -r development.txt

# copy project
COPY . .