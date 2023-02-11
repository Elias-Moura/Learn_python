''' super() é a super classe na sub classe
Classe principal (Pessoa)
    -> super class, base class, parent class
Classe filhas (Cliente)
    -> sub class, child class, derived class
'''


# Sobrescrever métodos ou adicionar funcionalidades a métodos da classe mãe (supper)

class MinhaSting(str):
    def upper(self):
        print('Chamou Upper')
        return super().upper()


minha_string = MinhaSting('Elias')
print(minha_string.upper())