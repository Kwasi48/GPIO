from gpiozero import LED
from time import sleep

red= LED(18)
yellow = LED(22)
green = LED(24)

while True:
    red.on()
    sleep(3)
    red.off()
    yellow.on()
    sleep(3)
    yellow.off()
    green.on()
    sleep(3)
    green.off()