"""
While em Python - Aula 7
utilizado para realizar ações equanto
uma confição for verdadeira.

Requisitos: entender condições e operadores_logicos
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue # pula o loop para a próxima verficiação
        # break para o loop

    print(x)
    x = x + 1


