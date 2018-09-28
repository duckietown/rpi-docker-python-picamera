
branch=$(shell git rev-parse --abbrev-ref HEAD)

tag=duckietown/rpi-docker-python-picamera:$(branch)

build:
	docker build -t $(tag) .

push:
	docker push $(tag)
