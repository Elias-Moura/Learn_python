# coding=utf8
# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Elias', 22)

# Podemos alterar os atributos (dados) de uma instância/objeto conforme abaixo:
p1.nome = 'Gabriel'
print(p1.nome)

# Podemos excluir um atributo com del:
p1.sobrenome = 'Silva' # Criando um tributo que não existia
print(p1.sobrenome)

del p1.sobrenome
# print(p1.sobrenome) # retorna AttributeError:  'Pessoa' object has no attribute 'sobrenome'
...
# Podemos ver todos os atributos de uma instância/objeto com objeto.__dict__ ou vars(objeto)

print(p1.__dict__)
print(vars(p1))

# Esse método não é apenas leitura. É possível criar novas chaves nesse dict:

p1.__dict__['altura'] = 1.80
print(vars(p1))

# A Classe não é serializavel -> é necessário criar uma lógica para acontecer.
# Por outro lado, você pode salvar os dados da sua instância/objeto em um JSON com o __dict__

'''Exemplo'''

dados_joao = {'nome': 'Joao', 'idade': 30, 'altura': 1.80}
joao = Pessoa(**dados_joao)  # Desempacotamento de dict

#  Quando desempacotamos um dict com ** ele retona os itens (chave e valor) assim:
#  nome='joão', idade=30, altura=1.80