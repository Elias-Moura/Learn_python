"""
Enumerate

Estrutura:
O enumerate permite que você percorra uma lista e ao mesmo tempo tenha
em uma variável o índice daquele item.
"""

# for item in lista:
#     resto do código

'''funcionarios = [
    'Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Paulo', 'Carlos',
    'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia',
    'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis'
    ]
for i, funcionario in enumerate(funcionarios):
    print(f'{i} é o funcionario {funcionario}')'''

'''Exemplo prático:
Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica há vários
produtos e não podemos deixar que o estoque caia abaixo dos 50 itens
'''

# Identifique quais produtos estão abaixo do nível mínimo de estoque:

estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 1100, 990, 900, 880, 870, 50, 1111, 120, 300, 450,800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho', 'caninha da roça', 'corona extra', 'corona baby', 'budwaiser', 'coquinha lata', 'vinho branco', 'guarana jesus', 'convesao', 'biscoito agua e sal', 'trakinas', 'ruffles']

for i, estoque_produto in enumerate(estoque):
    if estoque_produto < 50:
        print(f'{produtos[i]} está abaixo do estoque. Temos apenas {estoque_produto} quantidades')



