'''
Estrutura de repetição: for
Funcionamento:
for i in range(n):
    Repetir o código n vezes
'''

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]
tan = len(produtos)
print(tan)

for i in range(tan):
    print(f'{producao[i]} unidades produzidas de {produtos[i]}')

