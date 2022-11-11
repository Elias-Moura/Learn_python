'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''


#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1

#         [ início : final : passo ]
print(lista[1:4])

print('- '*10+'\n')
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(f'A lista l1 é {l1}')
print(f'A lista l2 é {l2}\n')


print('Podemos juntar listas usando o método extend')

l1.extend(l2) # ou l1 + l2

print(f"Está e a nova lista l1 {l1}")
print(f"Lista l2 {l2}\n")

print('para adicionar um valor ao final da lista utilizamos o método append')

l1.append(2000)
print(f'{l1} \n')

print('Para escolher onde você quer adicionar o valor (índice) use o método insert')

#         índice que vai entrar, valor desejado

l2.insert(0, "Olha ele aqui")
print(f'{l2} \n')


print('Para excluir um ítem da lista basta utilizar o método pop')

# Se você não passar o índice no método pop ele excluirá o último valor da lista (-1)
l2.pop(0)

print(f'{l2}\n')

print('para excluir vários itens de uma lista podemos utilizar del \n')

#     0  1  2  3  4  5  6  7  8  9
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'nova lista l3: {l3}')

#      início: fim sem incluir o índice
del(l3[3:6])

print(f'Os itens {l3[3:6]} serão excluidos.')
print(f'{l3}\n')

print('Para pegar o maior valor e o menor valor de uma lista basta usar max() e min():')

print(f'O maior valor da lista l3 é {max(l3)} e o menor valor é {min(l3)} \n')

print('Usando a função range e list para criar listas')

print('crie uma lista que comece no 1 e termine no 9')

# O método range retorna um objeto de tipo range, mas podemos fazer o casting para uma lista passando o método antes:
l4 = list(range(1, 10))
print(l4)




