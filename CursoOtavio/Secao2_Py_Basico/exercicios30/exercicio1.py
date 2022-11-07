'''
Faça um programa que peça ao usuário para digitar um número inteiro
infomr se este número é par ou ímpar. Caso o usuário não digite um num
inteiro, informe que não é m número int.
'''
print('-'*30)
print('Checando se é par.')
print('-'*30)

tent = 'y'
while tent == 'y':
    num1 = input('Digite o primeiro número: ')
    if num1.isnumeric():
        num1 = int(num1)
        if num1 % 2 == 0:
            print(f'{num1} é par.')
        else:
            print(f'{num1} não é par.')
    else:
        print(f'{num1} não é inteiro.')
        print('Digite um número inteiro para o programa funcionar.')
    tent = input('Quer tentar novamente? [y/n]').lower()

