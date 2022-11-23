#   Índices
#        0123456789......................33

frase = 'O rato roeu a roupa do rei de roma' # Iterável
tamanho_frase = len(frase)

nova_string = ''
rodatnoc = 0

# while rodatnoc < tamanho_frase:
#     print(frase[rodatnoc], rodatnoc)
#     rodatnoc += 1

input_do_usuario = input('Qual letra deseja colocar maiúcula? ')

# Iteração - Iterar
while rodatnoc < tamanho_frase:
    letra = frase[rodatnoc]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    rodatnoc += 1
print(nova_string)