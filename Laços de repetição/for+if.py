''' for + if
for item in lista:
    if condicao:
        faça alguma coisa
    else:
        outra coisa
'''
# Digamos que a gente esteja analisando a meta de vendas dos funcionários
# de uma empresa.A meta é de 1000 reais em 1 dia.
# Temos uma lista com as vendas de todos os funcionários e quero
# calcular qual o % de pessoas que bateram a meta
vendas = [
    1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100,
    999, 900, 880, 50, 1111, 120, 300, 450, 800
          ]
meta = 1000
bateu_meta = 0
for i in vendas:
    if i >= meta:
        bateu_meta += 1

funcionarios_totais = len(vendas)
porcentagem_meta = bateu_meta / funcionarios_totais

print(f'A quantidade de funcionário que bateram a meta foram: {bateu_meta}\n'
      f'A proporção foi de {porcentagem_meta:.0%}')
