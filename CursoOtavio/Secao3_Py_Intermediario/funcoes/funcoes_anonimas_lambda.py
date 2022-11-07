"""
funcoes anonimas - lambda function
"""


def func(arg, arg2):
    return arg * arg2


var = func(2, 2)
print(var)

lambda_exemplo = lambda x, y: x * y

var1 = lambda_exemplo(2, 2)
print(var1)

# exemplo prático:
# Quero ordenar uma lista de listar:

lista = [
    ['P1', 10],
    ['P2', 50],
    ['P3', 35],
    ['P4', 5],
    ['P5', 3]
]


# A função sorted não altera a lista origiral // o método .sort() sim
# lista.sort(key=lambda x: x[1]) altera a lista original

print(sorted(lista, key=lambda i: i[1], reverse=True)) # não altera a lista original
print(lista)

