#importing necessary libaries
from gpiozero import LED
from time import sleep

#create an object called led that refers to GPIO 23
groen= LED(23)
gul= LED(24)
roed= LED(25)
#create variable called delay that refers to delay time in seconds
delay=1

while True:
    #set led1 to on for the delay time
    groen.on()
    gul.on()
    roed.on()
    print('LED set to on')
    sleep(delay)
    #set led1 to off for the delay time
    groen.off()
    gul.off()
    roed.off()
    print('LED set to off')
    sleep(delay)
    

