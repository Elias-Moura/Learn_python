'''
Tipos de dados
str - string - textos 'exemplo' "exemplo"
int - inteiro -  -3 -2 -1 0 1 2 3 4 5 6 ...
float - real/ponto flutuante -5.08 0.0 1.0 2.3 ..
bool - booleano/lógico - True/False
'''

'''print('Elias', type('Elias'))
print('10', type(10))
print('1.0', type(1.0))
print('True', type(True))'''

# String: nome
nome = input('Qual é o seu nome? ')
print(nome, type(nome))

# Idade: int
idade = int(input('Qual é a sua idade? '))
print(idade, type(idade))

# Altura: float
altura = float(input('Qual é a sua altura? '))
print(altura, type(altura))

if idade >= 18:
    print('Parabéns, você já pode ser preso. ')
else:
    print('Fedendo a leite. ')

'''
Operadores Lógicos - Aula 4
and, or, not (inverte o retorno da lógina)
in e not in
'''