FROM python

RUN apt-get update  \
    && apt-get update  \
    && pip install django
RUN apt-get update  \
    && apt-get install default-mysql-server -y
RUN pip install mysql mysql-connector-python-rf

WORKDIR /usr/src/

COPY requirements.txt /usr/src

RUN pip3 install -r requirements.txt
