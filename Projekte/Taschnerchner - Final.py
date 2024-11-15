Rechnung=0
Ergebnis=[0]
Anzahl_Rechnungen = 1
Länge = 0
while Ergebnis[-1] != "=":
    Rechnung = input( "Bitte " + str(Anzahl_Rechnungen) + ". Zahl eingeben: ")
    Anzahl_Rechnungen += 1
    Ergebnis.append(Rechnung)
    Rechnung = input("Bitte Rechnenzeichen eingeben: ")
    Ergebnis.append(Rechnung)
Ergebnis.pop()
while len(Ergebnis) > 2:
    if Ergebnis[2] == "*":
        Rechnung = int(Ergebnis[1]) * int(Ergebnis[3])
        Ergebnis.insert(1 , Rechnung)
        Ergebnis.pop(2)
        Ergebnis.pop(2)
        Ergebnis.pop(2)
    elif Ergebnis[2] == "/":
        Rechnung = int(Ergebnis[1]) / int(Ergebnis[3])
        Ergebnis.insert(1 , Rechnung)
        Ergebnis.pop(2)
        Ergebnis.pop(2)
        Ergebnis.pop(2)
    elif Ergebnis[2] == "+" or Ergebnis[2] == "-":
        if len(Ergebnis) > 4:
            if Ergebnis[4] == "+" or Ergebnis[4] == "-":
                if Ergebnis[2] == "+":
                    Rechnung = int(Ergebnis[1]) + int(Ergebnis[3])
                    Ergebnis.insert(1 , Rechnung)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
                elif Ergebnis[2] == "-":
                    Rechnung = int(Ergebnis[1]) - int(Ergebnis[3])
                    Ergebnis.insert(1 , Rechnung)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
            elif Ergebnis[4] == "*":
                Rechnung = int(Ergebnis[3]) * int(Ergebnis[5])
                Ergebnis.insert(3 , Rechnung)
                Ergebnis.pop(4)
                Ergebnis.pop(4)
                Ergebnis.pop(4)
            elif Ergebnis[4] == "/":
                Rechnung = int(Ergebnis[3]) / int(Ergebnis[5])
                Ergebnis.insert(3 , Rechnung)
                Ergebnis.pop(4)
                Ergebnis.pop(4)
                Ergebnis.pop(4)
        else:
            if Ergebnis[2] == "+":
                    Rechnung = int(Ergebnis[1]) + int(Ergebnis[3])
                    Ergebnis.insert(1 , Rechnung)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
            elif Ergebnis[2] == "-":
                    Rechnung = int(Ergebnis[1]) - int(Ergebnis[3])
                    Ergebnis.insert(1 , Rechnung)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
                    Ergebnis.pop(2)
Ergebnis.pop(0)
print(Ergebnis)
input() 