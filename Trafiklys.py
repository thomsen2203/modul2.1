#importing necessary libaries
from gpiozero import LED
from time import sleep

groen= LED(23)
gul= LED(24)
roed= LED(25)

#roed.blink(1, 1)
#gul.blink(2, 2)
#groen.blink(3, 3)

delay=1

while True:
    roed.on()
    sleep(1)
    gul.on()
    sleep(1)
    groen.on()
    sleep(1)
    roed.off()
    sleep(1)
    gul.off()
    sleep(1)
    groen.off()
    sleep(1)

