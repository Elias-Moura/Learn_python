
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    multiplicado = 1
    for arg in args:
        multiplicado *= arg
    return multiplicado

var = multiplica(1,2,3,4,5)

print(var)

def par_ou_impar(x: int):
    if x % 2 == 0:
        return f'{x=} é par.'
    return f'{x=} é impar.'

print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(15))
