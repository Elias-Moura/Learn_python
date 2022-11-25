# coding=utf8
# Atributos da classe

class Pessoa:
    # Atributos da classe - está atrelado ao molde
    ano_atual = 2022
    # Se você alterar esse atributo ele vai mudar para todas as instâncias/objetos

    def __init__(self, nome, idade):
        # Atributos da instância/objeto

        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Elias', 22)
p2 = Pessoa('Gabriella', 23)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())