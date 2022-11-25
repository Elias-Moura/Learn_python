# coding=utf8

# Métodos em instâncias de classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.


class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def acelerar(self):
        print(f'{self.nome} está acelerando. ')


fusca = Carro('Fusca', 'VW')

print(fusca.marca)
fusca.acelerar()