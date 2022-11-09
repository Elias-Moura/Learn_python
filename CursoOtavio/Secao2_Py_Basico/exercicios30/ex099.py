"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe
que isso não é um número inteiro.
"""

numero_str = input('Digite um número inteiro ').strip()
numero_int = None
numero_par = None

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'O numero {numero_int} é par.')
    else:
        print(f'O número {numero_int} é impar.')
except:
    print('Isso não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, basenado-se no horário descrito, exiva a saudação
apropriada.
"""

horario_str = input('What time is it? [0 - 23]h ')
horario_int = None
bom_dia = 'Bom dia! '
boa_tarde = 'Boa tarde! '
boa_noite = 'Boa noite! '

try:
    horario_int = int(horario_str)
    if 11 >= horario_int >= 0:
        print(bom_dia)
    elif 17 >= horario_int >= 12:
        print(boa_tarde)
    elif 23 >= horario_int >= 18:
        print(boa_noite)
    else:
        print('Você digitou um horário inválido. ')
except:
    print('Você não digitou um valor válido')

