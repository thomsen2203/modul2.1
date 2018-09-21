#import time
from gpiozero import LED
from time import sleep
groen= LED(23)
gul= LED(24)
roed= LED(25)

def start():
    print("Start")
    return fibertyper

Multi850=2.5#dB/km
Multi1300=0.6#db/km
Single1310=0.35#db/km
Single1550=0.20#db/km

def Bruttooverskud(linktab):
    recieve=float(input("Indtast recieve sensitivity"))
    outputpower=float(input("Indtast output power"))              
    sum1=(recieve-outputpower-linktab)
    print("nettooverskud"+str(sum1))
    if sum1>0:
          print("Modul kan bruges")
          groen.on()
          return start
    else:
          print("kan ikke bruges, lav ny beregning")
          roed.on()
          return start




def fibertyper():
    fiber =int(input("Vælg fibertyper: 1.Singlemode eller 2.Multimode"))
    if fiber==1:
        print("Du har valgt singlemode")
        return singlemode
    elif fiber==2:
        print("Du har valgt multimode")
        return multimode
    else:
        print("prøv igen")
        return fibertyper 

def singlemode():
    Type=int(input("Vælg mellem: 1. 1310nm eller 2. 1550nm"))
    if Type ==1:
        print("Du har valgt 1310nm")
        return sm1310
    elif Type==2:
        print("Du har valgt 1550nm")
        return sm1550
    else:
        print("Du skal vælge 1 eller 2")
        return singlemode

def multimode():
    Type=int(input("Vælg mellem: 1. 850nm eller 2. 1300nm"))
    if Type ==1:
        print("Du har valgt 850nm")
        return mm850
    elif Type==2:
        print("Du har valgt 1300nm")
        return mm1300
    else:
        print("Du skal vælge 1 eller 2")


def sm1310():
    kmfiber=float(input("indtast fiber i Km"))
    Antalsp=float(input("Antal splidsninger"))
    Antalkon=float(input("Indtast Antal Konnektore"))
    SikMargin=float(input("Indtast Sikkerheds Margin"))
    Rep=float(input("Indtast Rep"))
    sum=(Single1310*kmfiber)+(Antalsp/10)+(Antalkon/2)+SikMargin+(Rep/2) 
    print(sum)
    print("dB")
    return Bruttooverskud(sum)
    
    

def sm1550():
    kmfiber=float(input("indtast fiber i Km"))
    Antalsp=float(input("Antal splidsninger"))
    Antalkon=float(input("Indtast Antal Konnektore"))
    SikMargin=float(input("Indtast Sikkerheds Margin"))
    Rep=float(input("Indtast Rep"))
    sum=(Single1550*kmfiber)+(Antalsp/10)+(Antalkon/2)+SikMargin+(Rep/2) 
    print(sum)
    print("dB")
    return Bruttooverskud(sum)
    
    

def mm850():
    kmfiber=float(input("indtast fiber i Km"))
    Antalsp=float(input("Antal splidsninger"))
    Antalkon=float(input("Indtast Antal Konnektore"))
    SikMargin=float(input("Indtast Sikkerheds Margin"))
    Rep=float(input("Indtast Rep"))
    sum=(Multi850*kmfiber)+(Antalsp/10)+(Antalkon/2)+SikMargin+(Rep/2) 
    print(sum)
    print("dB")
    return Bruttooverskud(sum)
    
    

def mm1300():
    kmfiber=float(input("indtast fiber i Km"))
    Antalsp=float(input("Antal splidsninger"))
    Antalkon=float(input("Indtast Antal Konnektore"))
    SikMargin=float(input("Indtast Sikkerheds Margin"))
    Rep=float(input("Indtast Rep"))
    sum=(Multi1300*kmfiber)+(Antalsp/10)+(Antalkon/2)+SikMargin+(Rep/2) 
    print("Sum er lig:"+str(sum)+"dB")
    return Bruttooverskud(sum)


    
    
    
    

state=start()
while state: state=state()

               



    
    
    
    

    


        
    
               


    

               
