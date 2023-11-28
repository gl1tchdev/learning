FROM ubuntu:latest
WORKDIR '/app'
COPY . .

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip install poetry