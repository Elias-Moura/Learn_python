# Crie funções que duplicam, triplicam e quadriplicam
# O número recebido como parâmetro.

def criar_multiplicador(numero):
    def multiplicar(fator):
        return f'{numero=} * {fator=} | {numero * fator}'
    return multiplicar

invertido = range(10,-1, -1)

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

for i, numero in enumerate(range(10)):
    var = criar_multiplicador(numero)
    print(var(invertido[i]))

