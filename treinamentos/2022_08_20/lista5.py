# ler 10 números e armazenar na lista
"""
lista = []
for i in range(10):
    lista.append(int(input()))
"""

lista = list(map(int, input().split()))

for elem in lista:
    print(type(elem), elem)
