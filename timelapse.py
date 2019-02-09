from gpiozero import Button, LED
from time import sleep, time
from picamera import PiCamera
import subprocess

userButton = Button(2)
red = LED(17)
irLED = LED(27)
camera = PiCamera()
camera.resolution = (1280, 720)
camera.color_effects = (128,128)
numberOfCaptures = 25200 
secondsInterval = 1
timeOfCapture = 0

irLED.on()
def wait(timeOfCapture):
    waitTime = 1 - time() + timeOfCapture;
    print('toc wait', waitTime)
    if waitTime > 0:
        sleep(waitTime)
        
def getStill(i):
    red.on()
    camera.capture(
        'image{0:06d}.jpg'.format(i),
        quality=10,
        )
    red.off()

for i in range(numberOfCaptures):
    timeOfCapture = time()
    getStill(i)
    wait(timeOfCapture)
    
camera.close()    
irLED.off()
subprocess.call('./convertStillsToVideo.sh')
