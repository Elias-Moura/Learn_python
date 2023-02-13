# coding=utf8

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leão = Animal('Leão')

print(leão.executar('Banana'))

"""
Uma varíavel definida dentro de um método não pode ser utilizada em outro método a não ser que você
utilize o self.nome_do_método/atributo.

A classe tem seu escopo e os métodos também.
"""

