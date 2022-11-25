# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da classe,
# mas não tem acesso ao self nem ao cls.
# em resumo, são funções que existem dentro da sua classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Sem desempacotar:', args, kwargs)
        print('Desempacotando:', *args)


c1 = Classe()

c1.funcao_que_esta_na_classe(1, 2, 3, nomeado='sou_nomeado', nomeado_2='esse também')