"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado para o parâmetro,
o valor padrão será usado.
Refatorar: editar o seu código.
"""

'''
Quando for necessário passar um valor padrão para uma função, de preferencia por
utilizar =None a utilizar =0 pois o 0 retorna falso em verificações.
ex: 

def resultado(a, b, c=0)
if c: #retornará falso e passará pelo bloco sem executar

para evitar esse problema e tornar possíveis as verificações use o None
    
'''
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

    return None # Isso já vem por padrão (implícito)

