nome = 'Elias Moura' # linguagem de tipagem dinamica
idade = 22
altura = 1.84
e_maior = idade > 18
peso = 95
imc = peso / altura ** 2


print('Nome: ', nome, type(nome))
print('Idade: ', idade, type(idade))
print('Altura: ', altura, type(altura))
print('E_maior: ', e_maior, type(e_maior))

print(nome, 'tem', idade, 'anos de idade e seu imc é ', imc)
# explicando format string
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{im:.2f}{n} tem {i} anos e seu imc é {n}'.format(n=nome, i=idade, im=imc))
