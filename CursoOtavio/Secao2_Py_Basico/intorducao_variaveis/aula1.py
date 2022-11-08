"""
Variáveis são usadas para salvar algo na memória do computador.
PEP8: inicie variáveis com letras minúsculas, pode usar números e undeline _.
O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um objeto.
Uso: nome_variavel = expresão
"""

nome = input('What is your name? ')
sobrenome = input('What is your last name? ')
idade = int(input('Qual é a sua idade? '))
ano_nascimento = 2022 - idade
maior_de_idade = idade >= 18
altura_metros = input('Qual é a sua altura? ')


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)