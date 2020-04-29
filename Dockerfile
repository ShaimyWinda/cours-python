#Download image
FROM ubuntu:16.04

RUN mkdir workspace && cd workspace

RUN apt-get update \
    && apt-get install -y python3  python3-pip vim git

RUN pip3 install jupyter ipython

RUN pip3 freeze > requirements.txt

RUN git clone https://github.com/ShaimyWinda/cours-python.git

RUN jupyter notebook --ip=127.0.0.1 --port=3000 --allow-root

EXPOSE 3000