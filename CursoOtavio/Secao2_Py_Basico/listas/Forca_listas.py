'''
Estudando listas em python
'''

from random import choice

palavras = [
    'borboleta',
    'criança',
    'abacate',
    'paralelepipedo',
    'gabriella',
    'azeitona',
    'python',
    'otorrinolaringologista'
]
secreto = choice(palavras)
digitadas = []
corretas = []
chances = ''

print(
    '\n'
    f'Regras: Você tem chances limitas a depender da dificuldade escolhida para acertar a palavra secreta \n'
    'Não vale digitar mais de uma letra \n'
    'Boa sorte! \n'
    )

dificuldade = ''
while dificuldade == '':
    dificuldade = input('Qual dificuldade você quer jogar? Fácil[F], Médio[M], Difícil[D] ')

    if dificuldade.upper() == 'F':
        chances = len(secreto) * 2
    elif dificuldade.upper() == 'M':
        chances = len(secreto) * 1.5
    elif dificuldade.upper() == 'D':
        chances = len(secreto) + 3
    else:
        print('Escolha a dificuldade correta. ')
        dificuldade = ''

print(f'Suas chances: {chances} ')
while True:
    if chances == 0:
        print('Você perdeu!')
        break

    # pegando uma letra do usuário

    letra = input('Digite uma letra: ')

    # tratando o caso de o jogador enviar mais de uma letra
    if len(letra) > 1:
        print('Não vale digitar mais de uma letra.')
        continue

    # Adicionando as letras digitadas em uma lista
    digitadas.append(letra)
    corretas.append(letra)


    # se a letra digitada está contida na palavra secreta mostre para o jogador, senão também.
    if letra in secreto:
        print(f'Acertou, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Errouuu, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        chances -= -1
        print(f'Você tem mais {chances} chances de acertar a palavra secreta')

        # Excluindo letras que não estão contidas na palavra secreta
        corretas.pop()

    # Criando uma variável de str vazia
    secreto_temporario = ''

    # para cada letra secreta na palavar secreta:
    for letra_secreta in secreto:

        # se a letra secreta está contida nas letras digitadas então:
        if letra_secreta in digitadas:
            # a variável secreto temporario recebe ela mesma mais a letra correta
            secreto_temporario += letra_secreta
        else:
            # Caso contrário ela recebe um *
            secreto_temporario += '*'

    print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f'Você ganhou e a palavra secreta é {secreto}')
        break
