"""
Funções (def) em Python - *args **kwargs -
Aula16 (Parte3)
"""
'''
*args é usado quando você quer deixar o número de argumentos da função livre
podendo ter 1 ou vários argumentos.

**kwargs = Keyword arguments ou argumentos de palavra-chave
como usar?

palavra-chave = 'chave'
exemplo: nome='Elias', idade=22, linguagem='Python'

Essas valores serão armazenados em um dicionário python e devem ser acessados conforme
a sua sintaxe:

Nesse caso será gerado:
kwargs{nome='Elias', idade=22, linguagem='Python'}

então, para acessar os itens:

kwargs['nome'], kwargs['idade'], kwargs['linguagem']
 
Lets code!
'''


def func(*args, **kwargs):
    print(args)  # Empacotado na tupla
    print(*args)  # Desempacotando -> pega cada valor e devolve
    # print(kwargs['nome']) # Dessa forma se o usuário não passar o nome python retornará um erro (KeyError: 'nome')
    nome = kwargs.get('nome')
    print(nome)  # Assim, caso o usuáro no passe o nome a var recebe None (não valor)

func(1, 2, 3, 4, 5, 6, 7, 8, 9, idade=22, linguagem='Python')