# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer as coisas
# @property - é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# geralmente é usada nas seguintes situações:
# - como getter
# - p/ envitar quebra código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# # Nas outras liguagens de programação:
# class Caneta:
#     def __init__(self, cor):
#         # private protected public
#         self.cor = cor
#
#     def get_cor(self):
#         return self.cor
#
#
# caneta = Caneta('Azul')
# print(caneta.get_cor())


class Caneta:
    def __init__(self, cor):
        # private protected public
        self.cor_tinta = cor

    @property     # getter
    def cor(self):
        return self.cor_tinta

    @property     # getter
    def cor_tampa(self):
        return "vermelha"


caneta = Caneta('Azul')
print(caneta.cor, caneta.cor_tampa)