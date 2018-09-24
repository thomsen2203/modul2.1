#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Print the celsius reading out.
"""
from gpiozero import LED
from DesignSpark.Pmod.HAT import createPmod
import time
import smtplib
groen= LED(23)
gul= LED(24)
roed= LED(25)


if __name__ == '__main__':
    
    therm = createPmod('TC1','JBA')
    time.sleep(0.1)
    



    try:
        while True:
            cel = therm.readCelcius()
            print(cel)
            if cel < 26:
                groen.on()
                gul.off()
            if cel >= 26:
                groen.off()
                gul.on()
            if cel >=30:
                roed.on()
                groen.off()
                gul.off()

                content = "ALARM!!! ALARM!!! DANGER BANG BANG !! AV MIN ARM"

                mail = smtplib.SMTP ("smtp.gmail.com",587)

                mail.ehlo()

                mail.starttls()

                mail.login("cozydille@gmail.com","Thomsen10")

                mail.sendmail("cozydille@gmail.com","christiangbach@gmail.com",content)

                mail.close()

            if cel <29:
                roed.off()


    
        

            #intn = therm.readInternal()
            #print(intn)
            time.sleep(0.8)
            
    except KeyboardInterrupt:
        pass
    finally:
        therm.cleanup()

