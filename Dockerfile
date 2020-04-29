#Download image
FROM ubuntu:16.04

RUN mkdir workspace && cd workspace

RUN apt-get update \
    && apt-get install -y python3  python3-pip vim git

RUN pip3 install jupyter ipython

RUN git clone https://github.com/ShaimyWinda/cours-python.git

EXPOSE 3000