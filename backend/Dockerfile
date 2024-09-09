FROM python:3.8.10-slim

WORKDIR /backend

COPY . /backend/
COPY .env /backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt