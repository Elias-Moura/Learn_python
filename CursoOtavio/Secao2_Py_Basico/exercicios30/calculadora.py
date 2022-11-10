
sair = None
numero_1_str = None
numero_2_str = None
operador = None
operadores_permitidos = '+-/*'
numero_1_float = None
numero_2_float = None
numeros_validos = None

while True:
    numero_1_str = input('Digite um número: ')
    numero_2_str = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    try:
        numero_1_float = float(numero_1_str)
        numero_2_float = float(numero_2_str)
        numeros_validos = True
    except Exception as error:
        print(error)
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue  # voltar para o início do while

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [S]im: ').upper().startswith('S')

    if sair:
        break # encerra o while

