# Docker(python + raspberry pi camera module) for ResinOS

This is a simple app that demonstrates how to create a Docker container for the Raspberry Pi camera module.
All it does is snap one photo every 3 seconds and then stores it in the /data directory on the PI.

A file server is running on the device port 8080, by using python's simplehhtpserver.
That way you can view the image taken by simply using resin's public url.

This example makes use of the awesome [picamera](http://picamera.readthedocs.org/en/release-1.8/) python module,
which natively controls the camera module and does not depend on raspistill.
