# ((5 ** 2 - 6 * 2 ** 2) * 3 + (13 - 7) ** 2 / 3) / 5

# ((5 ** 2 - 6 * 2 ** 2) * 3 + (13 - 7) ** 2 / 3) / 5)

# )((5 ** 2 - 6 * 2 ** 2) * 3 + (13 - 7) ** 2 / 3) / 5

# (((5 ** 2 - 6 * 2 ** 2) * 3 + (13 - 7) ** 2 / 3) / 5

qt = 0
exp = input()

correta = True

for elem in exp:
    if (elem == '('):
        qt += 1
    elif (elem == ')'):
        if (qt > 0):
            qt -= 1
        else:
            correta = False
            break

print(qt)

if (correta == True) and (qt == 0):
    print('Expressão correta')
else:
    print('Expressão inválida')
