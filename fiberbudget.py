
print("Optisk Fiberbudget")
mm850=2.5#dB/km
mm1300=0.6#db/km
sm1310=0,35#db/km
sm1550=0,20#db/km
margin=3#db  

#print("Indtast Km Fiber")
kmfiber=float(input("Indtast Km Fiber"))

#Indtast Antal Splidsninger
Antalsp=int(input("Antal splidsninger"))

#print("Indtast Antal Konnektore")
Antalkon=int(input("Indtast Antal Konnektore"))

#print("Indtast Sikkerheds Margin")
SikMargin=int(input("Indtast Sikkerheds Margin"))

#print("Indtast Rep")    
Rep=float(input("Indtast Rep"))

sum=(mm850*kmfiber)+Antalsp+Antalkon+SikMargin+Rep
print(sum)
print("db/km")

def fibertest():
    længde =float(input("Indtast fiber størrelse:"))
    if == 850:
        print("Du har valgt 850nm"






    
