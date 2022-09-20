'''
Uma variável deve:
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'Elias Moura' # linguagem de tipagem dinamica
idade = 22
altura = 1.84
e_maior = idade > 18
peso = 95
imc = peso / altura ** 2


print('Nome: ',nome, type(nome))
print('Idade: ',idade, type(idade))
print('Altura: ',altura, type(altura))
print('E_maior: ', e_maior, type(e_maior))

print(nome, 'tem', idade, 'anos de idade e seu imc é ', imc)
