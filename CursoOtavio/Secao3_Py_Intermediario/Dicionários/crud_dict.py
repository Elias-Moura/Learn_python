# Manipulando chaves e valores em dicionários

# Criando um dict
pessoa = {}

# Passando uma key para uma var
chave = 'nome'  

# Criando a chave 'nome' no dict pessoa
pessoa[chave] = 'Luiz Otávio'
# Criando a chave 'sobrenome' no dict pessoa (hardcoded)
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

# Sobreescrevendo no nome para 'Maria'
pessoa[chave] = 'Maria'

# Excluindo a chave 'Sobrenome' no dict pessoa
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# Verificando se a chave existe no dicionário.
#.get() retorna None como padrão o que permite fazer verificações
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')