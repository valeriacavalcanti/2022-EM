import random

lista = []
for i in range(10):
    lista.append(random.randint(1,100))

print(lista)

# exibir o 4 maior número lido
lista.sort()

print(lista)

lista.reverse()

print(lista)

print(lista[3])
