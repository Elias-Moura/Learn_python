# encondig=UTF-8
"""
Relação entre classes:
Associação, agregação e composição.
Composição é uma especialização da agregação mas nela, quando o objeto "pai" for apagado,
todas as referências dos objetos filhos também são apagadas.

"""

# composição -> é a relação mais forte,

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Elias')
cliente1.inserir_endereco('Rua Via Lactea', 135)
cliente1.inserir_endereco('Rua Visconde de st Isabel', 77)

cliente1.listar_enderecos()