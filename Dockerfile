FROM resin/raspberrypi3-python

#switch on systemd init system in container
ENV INITSYSTEM off

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8080

VOLUME ["/data"]

CMD ["bash","start.sh"]

