lista = list(range(2, 51, 2))
lista.append(-1)
lista.insert(0,-1)
lista.insert(4,-1)
lista.insert(10,-1)
lista.insert(16,-1)

print(lista)

while -1 in lista:
    lista.remove(-1)

print(lista)
