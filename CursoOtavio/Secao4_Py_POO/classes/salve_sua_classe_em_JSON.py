# Exercício - Salve sua classe em JSON
# Salve os dados da dsua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos
# Faça em arquivos separados

import json

CAMINHO_ARQUIVO = 'exerciciojsonclasse.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


elias = Pessoa('Elias', 22)
gabriella = Pessoa('Gabriella', 23)
irineu = Pessoa('Irineu', 45)


def adicioar_objetos_lista(*args):
    lista_pessoas_objects = [*args]
    lista_pessoas_objects = [
        vars(item)
        for item in lista_pessoas_objects
    ]
    return lista_pessoas_objects


def fazer_dump(lista_pessoas_objects):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_pessoas_objects, arquivo, ensure_ascii=False, indent=2)
        print('Dump feito com sucesso.')

# Como execuar a função somento quando eu estiver nesse módulo?
# Utilizar if name == main:


if __name__ == '__main__':
    print("fazendo o dump")
    fazer_dump(adicioar_objetos_lista(elias, gabriella, irineu))