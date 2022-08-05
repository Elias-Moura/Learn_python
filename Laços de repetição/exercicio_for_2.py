'''Análise de vendas
Temos uma lista com os vendedores e os valores de venda e queremos
identificar quais os vendedores que bateram a meta e qual foi
o valor que eles venderam
'''
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

meta = 10000

for item in vendas:
    if item[1] >= meta:
        print(f'O vendedor {item[0]} bateu a meta. Fez {item[1]} vendas')

