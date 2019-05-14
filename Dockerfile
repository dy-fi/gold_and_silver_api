FROM ubuntu:16.04

LABEL maintainer="Dylan Finn <dylanfinn89@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

# Cache dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install python-dateutil 
RUN pip3 install numpy

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]