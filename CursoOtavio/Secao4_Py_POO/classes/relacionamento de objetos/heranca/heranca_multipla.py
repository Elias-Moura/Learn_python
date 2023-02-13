'''
Herança múltipla - Python Orientado a Objetos
Quer dizer que no Python, uma classe pode estender várias outras

Herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente

Hernaça múltipla e mixins

Log -> Filelog
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Cliente(Pessoa, Filelog)

Python 3 usa C3 superclass linearization
para gerar o mro
Você não precisa estudar isso (é complexo)

Para saber a ordem de chamada dos métodos
use o método de class Classe.mro()
Ou o atributo __mro__ (Dunder - double underscore)
'''



