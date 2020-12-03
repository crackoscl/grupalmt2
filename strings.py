import random
from statistics import mean

caracteres = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz­_'
lista = []
lista_largo_de_lista = []
lista_promedio = []


for n in range(0,100):
    string_aleatorio = ''
    largo = random.randint(1,20)
    for i in range(0,largo):
        string_aleatorio += random.choice(caracteres)
    lista.append(string_aleatorio)

for i in lista:
    lista_largo_de_lista.append((len(i)))

largo_lista = len(lista)
promedio_lista = int( mean(lista_largo_de_lista))


for i in range(largo_lista):
    string_aleatorio = ''
    for i in range(promedio_lista):
        string_aleatorio += random.choice(caracteres)
    lista_promedio.append(string_aleatorio)


print('promedio entero')
print(promedio_lista)

print("strings largo de promedio de lista")

print(lista_promedio)

