print ("A. Orecchiette con cime di rapa")
print ("B. Pasta al pesto")
print ("C. Mezze maniche alla carbonara")
print ("D. Pasta al pomodoro")
scelta = input ("Scegli > ")
if scelta == "A":
    print ("Il piatto costa 10 euro")
    importo=10
    
elif scelta == "B":
    print ("Il piatto costa 11 euro")
    importo=11
    
elif scelta == "C":
    print ("Il piatto costa 12 euro")
    importo=12
    
elif scelta == "D":
    print ("Il piatto costa 13 euro")
    importo=13
    
numpiatti=int(input("Quanti piatti vuoi? "))
tot=numpiatti*importo
print("Totale: ", tot)