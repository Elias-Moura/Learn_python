"""
1- Crie uma função1 que recebe uma função2 como parâmetro e retone o valor da função executada
"""


def onefunc():
    return 'value'


def twofunc(arg):
    print(arg)


twofunc(onefunc())

"""
2- Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor
da funcao2 executada. Faça a funcao1 executar duas funçoes que recebam um número
diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def say_hi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'


executando = mestre(say_hi, 'Elias')
executando2 = mestre(saudacao, 'Elias', 'Bom dia')

print(executando, '\n', executando2)
