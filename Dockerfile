FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get clean

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/