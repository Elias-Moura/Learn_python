

while True:
    nome = input('Qual é o seu nome? ')

    print(nome or 'Você não digitou nada :( ')
    break

a = 0       # Retorna Falso
b = None    # Retorna Falso
c = False   # Retorna Falso
d = []      # Retorna Falso
e = {}      # Retorna Falso
f = 22      # Retorna Verdadeiro
g = 'Luiz'  # Retorna Verdadeiro

# Ele para assim que encontra um verdadeiro

variavel = a or b or c or d or e or f or g

print(variavel)

''' Isso é o mesmo que escreves condicionais assim:'''
# if a:
#     variavel = a
# elif b:
#     variavel = b