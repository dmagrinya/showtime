FROM python:3-alpine
RUN apk update && apk add postgresql-dev gcc build-base
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
