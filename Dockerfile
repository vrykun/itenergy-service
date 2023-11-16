FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /itenergy/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /itenergy/requirements.txt

COPY itenergy /itenergy/app
