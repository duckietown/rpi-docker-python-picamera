#!/usr/local/bin/python

import time
import picamera

while True:
    with picamera.PiCamera() as camera:
        #camera.resolution = (320, 240)
	camera.resolution = (2592, 1944)
	camera.resolution = (1920, 1080)
        # Camera warm-up time
        time.sleep(2)
        camera.capture('/data/image.jpg')

    print 'Picture taken'
    time.sleep(1)
