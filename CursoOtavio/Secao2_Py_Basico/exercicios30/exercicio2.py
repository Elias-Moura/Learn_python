'''
Faça um programa que pergunta a ora ao usuário e baseando-se no horário
descrito, exiba a saudação aproprioada. Ex.:
bom dia 0-11:59, boa tarde 12 - 17:59 e Boa noite 18- 23.59
'''

hora = input('Digite a hora: ')


hora = int(hora)
if 0 <= hora <= 11:
    print('Bom dia.')
elif 11 < hora <= 17:
    print('Boa tarde.')
elif 17 < hora <= 23:
    print('Boa noite.')
else:
    print('Digite um número de 0 a 23.')