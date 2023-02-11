'''
Herança simples - Relações entre classes
Associação - usa | Agragação - tem | Composição - é dono de
Herança - é um

Herança ou composição

Classe principal (Pessoa)
    -> super class, base class, parent class
Classes filhas (cliente)
    -> sub class, child class, derived class
'''

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('fui buscar na Class Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Eita, nem saí da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    ...


c1 = Cliente('Elias', 'Moura')
c1.falar_nome_classe()
a1 = Aluno('Gabriella', 'Andrade')
a1.falar_nome_classe()
