"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

''' print("""
Jogo da forca! \n
REGRAS:\n
1- Digite apenas letras;\n
2- Não vale digitar a palavra toda de uma vez
3


""") '''

from random import choice

PALAVRAS_FACEIS = (
    'borboleta',
    'criança',
    'abacate',
    'futebol',
    'americano',
    'sorvete',
    'bola',
    'azeitona',
    'vaca',
    'python',
    'amor',
    'livro',
)

PALAVRAS_MEDIAS = (
    'goleiro',
    'batedor',
    'numerador',
    'padeiro',
    'aldeído',
    'multimídia',
    'carteira',
    'planejar',
    'malandro',
    'médico',
)

PALAVRAS_DIFICEIS = (
    'otorrinolaringologista',
    'paralelepipedo',
    'policarbonato',
    'parabrisa',
    'lanterneiro',
    'idiossincrasia',
    'procrastinar',
)

PALAVRAS_PESADELO = (
    'aeropiesotermoterápico', 'acrocefalossindactilia', 'anticonstitucionalmente', 'anticonstitucionalismo',
    'celiossalpingectômico', 'cineangiocoronariográfico', 'coledocoduodenostômico', 'coronografopolarímetro',
    'cristaloluminescência', 'diacetilenodicarbonato', 'estereofotogramétrico', 'espectrocolorimétrico',
    'fotocromometalografia', 'fotocromometalográfico', 'hexanitrodifenilamina', 'hidropneumopericárdio',
    'histerossalpingectomia', 'histerossalpingografia', 'histerossalpingográfico', 'interconfessionalismo',
    'inconstitucionalidade', 'inconstitucionalissimamente', 'inconstitucionalmente', 'interdisciplinaridade',
    'meningoencefalomielite', 'multidisciplinaridade', 'oftalmotorrinolaringologista', 'otorrinolaringologista',
    'parassimpaticomimético', 'pneumartrorradiografia', 'preterintencionalidade', 'supertuberculinização',
    'transdisciplinaridade', 'traquelangulescapular', 'traquelatloidoccipital', 'ureteropielonefrítico',
    'ureteropieloneostômico'
)

palavra_secreta = ''
letras_acertadas = ''
CHANCES = ''
tentativas = 0
letras_erradas = ''
palavra_formada = ''
tentativas_restantes = 0
letras_restantes = ''
jogar_dnv = ''

while True:

    print('- ' * 30)
    if tentativas == 0:
        dificuldade = input('Escolha uma dificuldade: \n [F]ácil, [M]édia, [D]ifícil ou [P]esadelo.')

        if dificuldade.lower().startswith('f'):
            palavra_secreta = choice(PALAVRAS_FACEIS)
        elif dificuldade.lower().startswith('m'):
            palavra_secreta = choice(PALAVRAS_MEDIAS)
        elif dificuldade.lower().startswith('d'):
            palavra_secreta = choice(PALAVRAS_DIFICEIS)
        elif dificuldade.lower().startswith('p'):
            palavra_secreta = choice(PALAVRAS_PESADELO)
        else:
            print('Você não informou uma dificuldade válida. ')
            continue

        CHANCES = len(palavra_secreta) * 2
        print(f'Você tem um total de {CHANCES} tentativas, Boa sorte!')
        print()

    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez')
        print('- ' * 30, '\n')
        continue

    if letra_digitada.isnumeric():
        print('Não digite números. ')
        print('- ' * 30, '\n')
        continue

    if letra_digitada in letras_acertadas:
        print('Você já acertou essa letra, digite outra.')
        print('- ' * 30, '\n')
        continue

    if letra_digitada in letras_erradas:
        print('Você já tentou essa letra e ela não existe na palavra secreta. ')
        print('- ' * 30, '\n')
        continue

    if letra_digitada in palavra_secreta:
        print('Você acertou a letra! ')
        # Cri uma "memória" das letras já acertadas
        letras_acertadas += letra_digitada
        tentativas += 1
    else:
        print(f'A letra "{letra_digitada}" não existe na palavra secreta. ')
        letras_erradas += letra_digitada
        tentativas += 1

    # Lógica para criar os ****** nas letras:
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    # Contador de tentativas
    tentativas_restantes = CHANCES - tentativas

    print(palavra_formada)

    print(f'letras erradas: {letras_erradas}')
    print(f'Tentativas restantes {tentativas_restantes}')

    # contando quantas letras faltam serem descobertas

    letras_restantes = palavra_formada.count('*')

    if letras_restantes > 1:
        print(f'--> {letras_restantes} letras secretas restantes.')
        print('- ' * 30, '\n')
    else:
        print(f'--> {letras_restantes} letra secreta restante :D.')
        print('- ' * 30, '\n')

    # Caso ganhador

    if palavra_formada == palavra_secreta:
        print('\n', '-*-' * 30, sep='')
        print(f'Você venceu o jogo!, a palavra secreta é "{palavra_secreta}".')
        print(f'Com um total de {tentativas} tentativas')
        print('-*-' * 30, '\n')

        # limpando as variáveis:
        letras_acertadas = ''
        tentativas = 0
        letras_erradas = ''
        palavra_formada = ''
        tentativas_restantes = 0

        jogar_dnv = input('Deseja jogar de novo? [S]im ou [N]ao \n')

        if jogar_dnv.lower().startswith('s'):
            continue
        else:
            print('\n', 'Obrigado por jogar! Tchau :)', sep='')
            break

    # Caso perdedor:

    if tentativas_restantes == 0 or letras_restantes > tentativas_restantes:
        print('...  T-T ... ' * 7, '\n')
        print(
            f"Você perdeu :'(, a palavra secreta era {palavra_secreta.title()}.\n"
            f'Total de tentaivas {tentativas}. \n'
            f'Letras digitadas {letras_erradas + letra_digitada} \n'
        )
        print('...  T-T ... ' * 7, '\n')

        # limpando as variáveis:
        letras_acertadas = ''
        tentativas = 0
        letras_erradas = ''
        palavra_formada = ''
        tentativas_restantes = 0

        jogar_dnv = input('Deseja jogar de novo? [S]im ou [N]ao ')

        if jogar_dnv.lower().startswith('s'):
            continue
        else:
            print('\n', 'Obrigado por jogar! Tchau :)', sep='')
            break
