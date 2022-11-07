'''
Tuplas
Semelhante a listas, porém:
1- Não podem ser modificadas (seus itens, ordem e etc...)
2- Podem ser homogeneas ou eterogeneas.
'''

t1 = 1,  # isso é retorna uma tupla.
t2 = 1, 2, 3, 4  # isso também é uma tupla.
t3 = (1, 2, 3, 4, 'Elias', 5, 6)  # tupla :)

# Podemos concatenar tuplas

t4 = t1 + t2
print(t4)

# Podemos desempacotar tuplas

#          pegando vário idx e pegando o último idx
n1, n2, n3, *_, n10 = t3

print(n3, n10)


# Podemos multiplicar uma tupla. - vai repetir seus itens.

trep = t4 * 10

print(trep)

# Podemos tranformar uma tupla em uma lista para modificar um item e depois voltar a ser tupla.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

tupla = list(tupla)

tupla[1] = 'Limão'

tupla = tuple(tupla)

print(tupla)