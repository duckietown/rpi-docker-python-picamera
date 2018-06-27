#!/usr/bin/env python

import time
import picamera

while True:
    with picamera.PiCamera() as camera:
	#camera.resolution = (2592, 1944) # camera max
	#camera.resolution = (1920, 1080) # 1080p
	camera.resolution = (1280, 720)   # 720p
        #camera.resolution = (320, 240)
        # Camera warm-up time
        time.sleep(2)
        camera.capture('/data/image.jpg')

    print 'Picture taken'
    time.sleep(1)
