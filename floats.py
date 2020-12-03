import random
from statistics import mean
lista = []
lista_normalizada = []


for n in range(0,100):
    numeros = round(random.uniform(10,50),3)
    lista.append(numeros)

promedio_lista = mean(lista)
maximo = max(lista)

for i in lista:
    lista_normalizada.append((i - promedio_lista)/ maximo)

print(promedio_lista)
print(lista)
print(maximo)
print("lista normalizada")
print(lista_normalizada)


