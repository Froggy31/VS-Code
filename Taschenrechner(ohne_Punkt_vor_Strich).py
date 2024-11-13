Anzahl=1
Zahl=0
Rechenzeichen=0
Gleich = "Hallo"
Nicht_Weiter=str(False)

Zahl= input ("Bitte " + str(Anzahl) + ". Zahl eingeben: ")
Anzahl+=1
while Nicht_Weiter==str(False): 
    Rechenzeichen= input ("Bitte Rechenzeichen eingeben: ")
    if Rechenzeichen== "+":
        Zahl =int(Zahl) + int(input ("Bitte " + str(Anzahl) + ". Zahl eingeben: "))
        Anzahl+=1
    if Rechenzeichen== "*":
        Zahl =int(Zahl) * int(input ("Bitte " + str(Anzahl) + ". Zahl eingeben: "))
        Anzahl+=1
    if Rechenzeichen== "-":
        Zahl =int(Zahl) - int(input ("Bitte " + str(Anzahl) + ". Zahl eingeben: "))
        Anzahl+=1
    if Rechenzeichen== "/":
        Zahl =int(Zahl) / int(input ("Bitte " + str(Anzahl) + ". Zahl eingeben: "))
        Anzahl+=1
    if Rechenzeichen == "=":
        print(Zahl)
        Nicht_Weiter=input ("Rechner beenden:")
        if Nicht_Weiter ==str(False):
            Zahl=0
            Anzahl=1
            Zahl= input ("Bitte " + str(Anzahl) + ". Zahl eingeben: ")





