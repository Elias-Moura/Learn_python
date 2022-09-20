'''
Criar variáveis com nome (srt), idade (int),
altura (float) e peso (float) de uma pessoa
Criar vairável com o ano atual (int)
Obter o ano de nascimento da pessoa (baaseado na idade e no ano atual)
Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

from datetime import datetime

nome = str(input('Digite o seu nome: '))
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
ANO_ATUAL = int(datetime.today().strftime('%Y'))
ano_nacimento = ANO_ATUAL - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nacimento}.')





