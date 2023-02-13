'''
Polimorfismo em Python Orientado a Objetos
Polimorfismo é o princípio que permite que classes defivadas de uma mesma superclass
tenham métodos iguais (com mesma assinatura) mas comportamentos diferentes

Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)

Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retornos iguais

SO"L"ID

Princípio da substituição de Liskov

Objetos de uma superclasse devem ser substituíveis por
objetos de uma subclasse sem quebrar a aplicação

Sobrecarga de métodos (overload) Python não suporta
Sobreposição de métodos Py suporta
'''

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('E-mail: enviando - ', self.mensagem)
        return True  # deveria ter uma lógica para retornar Ture ou false


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando - ', self.mensagem)
        return False
