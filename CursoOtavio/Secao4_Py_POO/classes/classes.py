# coding=utf8

"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instânvias) que
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classes.
"""

# Atributos -> dados dentro da classe
# métodos -> ações que a classe pode executar


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Elias', 'Moura')
# p1.nome = 'Elias'
# p1.sobrenome = 'Moura'

print(p1.nome, p1.sobrenome)

