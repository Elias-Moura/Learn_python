# Métodos de calsse + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, recebemos a própria classe.

class Pessoa:
    ano = 2023  # Atributo da classe -> Molde

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # decorando o método da instância para se torar método da classe

    @classmethod
    def metodo_de_classe(cls):  # cls = abreviação para classe (convenção)
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

    #  Isso gera uma extençaõ para o seu molde (classe)
    #  também pode ser chamado de factori


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(32)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


