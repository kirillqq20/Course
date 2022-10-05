FROM ubuntu:20.04

LABEL maintainer="kruskrush17@gmail.com"

ENV Status="OK"

ENV TZ=Europe/Kiev

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install net-tools -y

RUN apt-get install apache2 -y

COPY . .

RUN mv ./index.html /var/www/html/

RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

CMD ["apachectl", "-D", "FOREGROUND"] && \
    [ "/bin/bash", "./task4.sh" ]

RUN service apache2 restart

VOLUME /devops_volume

EXPOSE 80