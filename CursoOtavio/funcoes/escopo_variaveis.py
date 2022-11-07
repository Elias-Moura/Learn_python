'''
Aula 17
escopo em funções
'''

"""
Tudo que esta dentro de uma funcao só existe dentro da funcao. (escopo local)

Para usar variáveis que estão no (escopo global - fora da func) passar como argumento.

Nunca utilizar 'global variavel' para utilizar o valor da variável global pois isso
gera comportamentos inesperados para a sua aplicação.

"""


variavel = 'valor'

def func():
    print(variavel)

