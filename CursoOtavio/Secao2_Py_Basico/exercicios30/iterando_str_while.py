frase = 'O Python é uma linguaguem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.' \
    .replace(' ', '').lower()

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
letra_atual = None
quantas_vezes_letra_apareceu = None

while i < len(frase):
    letra_atual = frase[i]

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_ganhadora = letra_atual


    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1

print(f'A letra que apareceu mais vezes foi {letra_ganhadora}.')