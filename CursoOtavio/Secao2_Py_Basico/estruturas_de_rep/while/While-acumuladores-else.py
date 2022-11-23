'''
While /Else - Aula 8
contadores
acumuladores
'''

rodatnoc = 1
acumulador = 1

while rodatnoc <= 10:
    print(rodatnoc, acumulador)

    if rodatnoc > 5:
        pass

    acumulador = acumulador + rodatnoc
    rodatnoc += 1
else:
    print('Cheguei no else.')

print('Isso aqui não é do else.')
