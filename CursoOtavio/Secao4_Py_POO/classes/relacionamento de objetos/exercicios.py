'''
Exercícios com classes
1- Crie uma classe Carro (nome)
2- Crie uma classe Motor (nome)
3- Crie uma classe Fabricante (nome)
4- Faça a ligação entre Carro tem Motor
Obs.: Um motor pode ser de vários carros
5- Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes na tela
'''


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = ''
        self._fabricante = ''

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def __repr__(self):
        return f'{self.nome}, {self.fabricante}, {self.motor}'

class Motor:
    def __init__(self, nome, litragem):
        self.nome = nome
        self.litragem = litragem

    def __repr__(self):
        return f'{self.nome}, {self.litragem}.'

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    def __repr__(self):
        return self.nome

carro = Carro('911 GT3 RS')
carro.motor = Motor('Boxer', '2.5')
carro.fabricante = Fabricante('Porsche GP Volks')

print(carro)