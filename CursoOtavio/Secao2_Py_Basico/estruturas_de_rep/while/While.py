'''

continue -> pula para o próximo laço de repetição
Break -> finaliza o loop tanto While quanto For

'''
from _ast import While

'''
x = 0 # coluna


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x +=1

print('acabou')
'''

# Calculadora simples
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Digite um operador válido.')

    sair = input('Deseja sair? [s]im ou [n]ão')
    if sair == 's':
        break