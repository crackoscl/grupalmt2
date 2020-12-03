import random
from statistics import mean
lista = []
lista_resta_promedio =  []

for n in range(0,100):
    for i in range(0,20):
        numeros = random.randint(1,20)
    lista.append(numeros)

promedio_lista = int(mean(lista))


for i in lista:
    resta = (i - promedio_lista)
    lista_resta_promedio.append(resta)    


print(lista)
print(promedio_lista)
print(lista_resta_promedio)