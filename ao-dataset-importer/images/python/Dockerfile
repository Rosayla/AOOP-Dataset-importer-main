FROM python:3.9.15-slim

WORKDIR /usr/src/app

RUN apt update
RUN apt install curl -y

# upgrade pip
RUN python -m pip install --upgrade pip

# install pg_config
RUN apt update && apt install libpq-dev -y
RUN apt install build-essential -y

# dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt