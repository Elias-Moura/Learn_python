# M�dulos padr�o do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: voc� tem o namespace do m�dulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do m�dulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: voc� pode reservar nomes para seu c�digo
# Desvantagens: pode ficar fora do padr�o da linguagem

# m� pr�tica - from nome_modulo import *
# Vantagens: importa tudo de um m�dulo
# Desvantagens: importa tudo de um m�dulo
# from sys import exit, platform

# print(platform)
# exit()