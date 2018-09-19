from random import random
from time import sleep
from gpiozero import LED
green= LED(23) 
yellow= LED(24)
red= LED(25)

def state0():
    #while True:
    green.on()
    yellow.off()
    red.off()
    print("green")
    sleep(1.0)
    return state1

def state1():
    #while True:
    red.on()
    green.off()
    yellow.off()
    print ("red")
    sleep(1.0)
    return state2
    
def state2():
    #while True:
    yellow.on()
    red  .off()
    green.off()
    print("yellow")
    sleep(1.0) 
    return state0

state=state0
while state: state=state()
print("slut")
