"""
Dicionários em Python
para declarar um dicioário basta abir e fechar chaves:
dic = {}

É utilizado o sisitema de chave valor:

       chave    valor    chave   valor  chave    valor
dic = {'nome': 'Elias', 'idade': '22', 'País': 'Brazil'}

e para acessar um valor do diciário utilizamos:

dic['Nome da chave']

"""

# Criando um dicionário

Elias = {'Nome': 'Elias', }

# Adicionando item ao dicionário
#     chave    valor
Elias['Idade'] = 22

print(Elias)

# Também podemos usar a função dict para criar um dicionário:
#                chave valor       chave valor
Gabriella = dict(Nome='Gabriella', idade=23, )

print(Gabriella)

# As chaves devem ser unícas - não podem existir duas chaves com o mesmo nome:

d1 = {'chave': 'valor', 'chave': 'valor não exibido', 'chave': 'valor real da chave', }
# vai exibir a última chave da sequencia de repetidas.

print(d1)

# O que é suportado como chave para um dict?

dict1 = {
    'str' : 'valor',  # strings
    123 : 'Outro valor',  # inteiros
    (1,2,3,4) : 'Tupla'  # tuplas
}

# Caso alguém tente acessar uma chave que não existe no dicionário
# O Python retornará uma excessao

# print (dict1['naoexiste']) # retorna o erro

''' Como contornar ?'''

if 'naoexiste' in dict1: # verificando se a chave existe no dict
    print(dict1['naoexiste'])
else:
    print('a chave "nãoexiste" não abre nenhum baú.')



'''Podemos criar uma chave se ela não existe:'''

if 'noexiste' not in dict1:
    dict1['noexiste'] = 'Agora existe'
    print(dict1['noexiste'])

'''
Ou ainda, podemos usar o método .get:
caso a chave não exista ele irá retornar None (não valor)
'''

print(dict1.get('nomedachave'))

# Podemos verificar se é none ou não e criar um bloco if:

if dict1.get('nomedachave') is not None:
    print('Essa chave existe :)')
    print(dict1.get('nomedachave'))
else:
    print('Chabe n existe :(')

# Outra maneira de atualizar ou adiconar uma chave e seu valor é usando o método .uptade
# ele recebe um dicionário com os valores

# Trocando
dict1.update({'str': 'strings'})


# Adicionando
dict1.update({'Robbie': 'Programar'})

print(dict1)

# Concatenando

d1 = {1: 2, 2: 3, 4: 5}
d2 = {'a': 'b', 'c': 'd'}

d1.update(d2)

print(f'Concatenando dicionários {d1}')


# Para excluir uma chave do dicionário utilizamos del nome-do-dic['nome da chave']

del dict1['str'] # Ou dict1.pop('chave') ou dict1.popitem() <- exclui a última chave

print(dict1)


# Para verificar se alguma chave já existe no dicionário:

print('str' in d1)  # retorna True/False # ou d1.keys()


# Para verificar se algum valor já existe:

print('valor' in d1.values())  # retorna True/False



# Para saber quantos pares de chabe valor existem dentro de um dicionário:

print(len(dict1))  # retorna a quantidade de pares key/value:



# Podemos iterar um dicionário com for:

dict1 = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3',}

for k in dict1: # retorna as chaves ou dict1.keys()
    print(k)

for v in dict1.values(): # retorna os valores
    print(v)

for i in dict1.items(): # retorna os pares chave valor em uma tupla
    print(i)

for key, value in dict1.items(): # retorna os items desenpacotados
    print(key, value)



# Podemos criar dict dentro de dict e iterar eles:

clientes = {
    'cliente1': {
        'nome': 'Elias',
        'sobrenome': 'Moura',
    },
    'cliente2': {
        'nome': 'Gabriella',
        'sobrenome': 'Andrade',
    },
    'cliente3': {
        'nome': 'Eduardo',
        'sobrenome': 'Mendes',
    },
}

# para cara chave e valor no dicionário clientes me exiba a chave:
for chave_clientes, values_clientes in clientes.items():
    print(f'Exibindo {chave_clientes}')

    # para cada chave e valor no dict que está dentro do dict clientes me exiba a key e o value:
    for dados_keys, dados_values in values_clientes.items():
        print(f'\t{dados_keys} = {dados_values}')


"""
Em python, mesmo você associando um dict a uma variável e alterar apenas o valor da variável
o valor no dicionário também será alterado pois os dois apotam para o mesmo valor na memória
do computador.
"""
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1

#v[1] = 'Elias'

print(v, d1)

"""
Caso você use o método da classe dicionário copy você terá uma cópia rasa do dicionário.
E, em alguns casos, o dicionário de origem também será alterado em caso de objetos diferentes de tuplas.

Para evitar isso será necessário importar o módulo copy e usar o médoto copy.deepcopy() 

var = copy.deepcopy(dicionário que quer copiar aqui)    
"""
import copy

v = copy.deepcopy(d1)
v[1] = 'Zarathustra'

print(v, d1)


"""
Também podemos transformar outros objetos em dicionários, como tuplas e listas:
"""

lista = [
    ['key0', 'value0'], #Também funciona com tuplar ()
    ['key1', 'value1'],
    ['key2', 'value2'],
]

d1 = dict(lista)

print(d1)
