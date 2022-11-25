# coding=utf8
# @property @setter - getter e setter no modo Pythonico
# - como getter
# p/ evitar quebrar o código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# Atributos que começam com um ou sou underlines não devem ser utilizados fora da classe

class Caneta:
    def __init__(self, cor):
        self._cor = cor


    @property
    def cor(self):
        print('PROPERTY -getter')
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor


caneta = Caneta('Azul')
# getter -> obter valor

print(caneta.cor)