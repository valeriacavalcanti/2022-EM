"""
   Escreva um programa para ler vários números, encerra quando for digitado valor 0.
   Exiba:
   - 4 maior valor lido.
   - Menor valor lido.
   - Maior valor lido.
   - Soma dos números lidos.
   - média dos números lidos
"""

lista = []
while True:
    num = int(input())
    if (num == 0):
        break
    lista.append(num)

lista.sort()
lista.reverse()
distintos = set(lista) # elimina as repetições
distintos = list(distintos)
distintos.sort()
distintos.reverse()

print(lista)
print('quarto maior:', distintos[3])
print('maior:', max(lista))
print('menor:', min(lista))
print('soma:', sum(lista))
print('média:', sum(lista)/len(lista))
