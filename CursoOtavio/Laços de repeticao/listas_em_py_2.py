'''
Split, Join, Enumerate em Python
* Split - dividir uma string # método de str que funciona com listas
* Join - Juntas uma lista # str
* Enumerate - Enumerar elementos da lista # Iteráveis
'''

# Usando Split
string = "O Brasil é o pais do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista_1:
    break
    qtd_vezes = lista_1.count(valor)
    print(f'iterando {valor} apareceu {qtd_vezes}x ')

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
        print(f' contagem {contagem} e a palavra {palavra}')


# print(f'A palavra que apareceu mais vezes é {palavra} {contagem}x')

# Usando join para juntar listas

executar = False

if executar == True:
    string = 'O Brasil é penta'  #sting padrão

    lista = string.split(' ')  #retirando os espaços retorna uma lista de strings

    string2 = '_'.join(lista)  #juntos a lista de strings com o separador underline retorna uma string

    print(string)
    print(lista)
    print(string2)

string_2 = 'O Brasil é penta.'
lista = string_2.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
