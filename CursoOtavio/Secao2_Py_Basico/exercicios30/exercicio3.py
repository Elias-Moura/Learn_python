'''
Faça um programa que peça o primero nome do usuário. Se o nome tiver
4 letras ou menos escreva"seu nome é curto", se tiver entre 5 e 6 letras
escreva seu nome é normal, maior que 6 "su nome é muito grande.
'''

nome = input('Digite o seu nome: ')

if nome:
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif 5 <= len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')