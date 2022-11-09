
while True:
    cpf = input('Digite um CPF: ')
    cpf = cpf.strip().replace('.', '').replace('-', '')
    cpf_inicio = cpf

    # Verificando se temos 11 caracteres digitados (como string)

    if not cpf.isnumeric() or len(cpf) != 11:
        print(
            'Digite o CPF no formato a abaixo e com números: \n'
            'xxx.xxx.xxx-xx'
        )

    decrescente = 10
    soma = 0
    for idx, value in enumerate(cpf):
        if decrescente == 1:
            break
        soma += int(cpf[idx]) * decrescente
        # print(cpf[idx], decrescente, soma)
        decrescente -= 1

    digito1 = 11 - (soma % 11)

    if digito1 > 9:
        digito1 = 0

    decrescente = 11
    soma = 0
    cpf = cpf[:-2] + str(digito1)

    for idx, value in enumerate(cpf):
        if decrescente == 1:
            break
        soma += int(cpf[idx]) * decrescente
        # print(cpf[idx], decrescente, soma)
        decrescente -= 1

    digito2 = 11 - (soma % 11)

    if digito2 > 9:
        digito2 = 0

    cpf_final = cpf_inicio[:-2] + str(digito1) + str(digito2)

    if cpf_final == cpf_inicio:
        print('CPF Válido.')
    else:
        print('CPF Inválido.')

    parar = input('Deseja parar?[S/N] ')
    if parar.upper() == 'S':
        break


