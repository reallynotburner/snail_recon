from gpiozero import Button, LED
from time import sleep, time
from picamera import PiCamera
import subprocess
import datetime as dt

userButton = Button(2)
red = LED(17)
irLED = LED(27)
camera = PiCamera()
camera.resolution = (1280, 720)
camera.color_effects = (128,128)
numberOfCaptures = 10 
secondsInterval = 1
timeOfCapture = 0

irLED.on()
def wait(timeOfCapture):
    waitTime = 1 - time() + timeOfCapture;
    if waitTime > 0:
        sleep(waitTime)
        
def getStill(i):
    red.on()
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.capture(
        'image{0:06d}.jpg'.format(i),
        quality=10,
        )
    red.off()
    print('captured ', i, ' of ', numberOfCaptures, ' images.')


for i in range(numberOfCaptures):
    timeOfCapture = time()
    getStill(i)
    wait(timeOfCapture)
    
camera.close()    
irLED.off()
subprocess.call('./convertStillsToVideo.sh')
