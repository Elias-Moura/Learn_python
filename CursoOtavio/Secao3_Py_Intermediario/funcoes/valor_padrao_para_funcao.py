"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Como verificar se mo usuário mandou ou não o argumento para o parametro 'z' ?
# Usar o None como argumento (Valor) padrão e usar um IF z is not None:

def soma(x, y, z= None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y )




soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')