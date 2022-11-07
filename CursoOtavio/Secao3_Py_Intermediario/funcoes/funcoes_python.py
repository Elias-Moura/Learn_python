"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


def say_hi(nome: str, saudacao: str):
    """

    :param nome: str
    :param saudacao: str
    :return: print(nome, saudacao)
    """
    print(nome, saudacao)


# nome = input('Qual é o seu nome? ')
nome = 'Elias'
saudacao = 'seja bem vindo.'

say_hi(nome, saudacao)

"""
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""

n1 = 2  # float(input('Digite um número: '))
n2 = 2  # float(input('Digite outro número: '))
n3 = 2  # float(input('Digite outro número: '))


def soma(n1, n2, n3):
    """
    :param n1: float
    :param n2: float
    :param n3: float
    :return: n1 + n2 + n3
    """
    return n1 + n2 + n3


print(f'A soma é {soma(n1, n2, n3)}.')

"""
3- Crie uma funcao que receba 2 números.
O primeiro é um valor e o segundo um percentual ex. 10%.
retorne o valor do preimeiro numero somado ao aumento percentual do mesmo.
"""

valor = 100
aumento = 0.1


def aumento_percentuarl(valor, aumento):
    """
    Retorna o valor acrescindo de uma procentagem do mesmo.
    :param valor: float
    :param aumento: float
    :return: valor * (1 + aumento)
    """
    return valor * (1 + aumento)


resultado = aumento_percentuarl(valor, aumento)

print(f' O aumento percentual de {aumento:.0%} do valor {valor} é igual a {resultado:.2f}')

"""
4- Fizz Buzz - Se o parâmetro da funcao for divisivel por 3, retorne fizz,
se o parametro da funcao for divisivel por 5 retorne buzz.
Se o parametro da funcao for divisivel por 5 e por 3, retorne FizzBuzz, caso contrário,
Retorne o número enviado.
"""


def fizz_buzz(number):
    """

    :param number: int
    :return:
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number


for i in range(10**2):
    value = fizz_buzz(i)
    print(f'O valor {i} é {value}')
