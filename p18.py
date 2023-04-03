import random 
lista=[]
for i in range (6):
    lista.append(random.randint(1,9))

for x in lista:
    print("> ", x)

numero = int(input("Dammi un numero"))