'''
Crie um jogo de perguntas e respostas usando dicionários e laçõs de repetição
'''

print('Texto explicativo. ')
print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '4',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5*2? ',
        'respostas': {
            'a': '10',
            'b': '2',
            'c': '4',
        },
        'resposta_certa': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10/2? ',
        'respostas': {
            'a': '1',
            'b': '5',
            'c': '4',
        },
        'resposta_certa': 'b'
    },
}

print()

# Iterando o dicionário.
# perguntas.items() -> retornará a chave e o valor.
# pk = as chaves do dict perguntas e pv = recebe os valores.

respostas_certas = 0
for pk, pv in perguntas.items():
    # acessando o dict e exibindo na tela as perguntas.
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')

    # acessando as respostas e exibindo na tela.
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: Respostas: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou.')
        respostas_certas += 1
    else:
        print('Você errou.')

    print()

qtde_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtde_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem foi de {porcentagem_acerto:.0f}%.')
