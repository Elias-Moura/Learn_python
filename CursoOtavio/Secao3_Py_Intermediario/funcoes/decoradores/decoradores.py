# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são fun~]oes que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outas funções


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar.')
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        print('Voce foi decorada.')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string.")




string = 'Batatinha'

invertida = inverte_string(string)

print(invertida)