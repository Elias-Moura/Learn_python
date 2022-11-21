# Variáveis livres + nonlocal

'''
A variável a é considerada livre pois ela não está
sendo definida dentro do escopo da funcao dentro.
'''

# def fora(x):
#     a = x
#     def dentro():
#         return a
#     return dentro
#
# dentro = fora(1)


def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        # Use o nonlocal para alterar o valor de uma variável definida em outro escopo
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))


