from gpiozero import Button, LED
from time import sleep

userButton = Button(2)
red = LED(17)
irLED = LED(27)

while True:
    irLED.on()
    if userButton.is_pressed:
        break
    
irLED.off()