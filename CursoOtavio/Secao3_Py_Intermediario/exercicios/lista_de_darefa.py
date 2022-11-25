# coding=UTF8
import json
import os
import sys


def listar(tarefas):
    #  Guard clause
    print()
    if not tarefas:
        print('Não há tarefas para listar')
        print()
        return
    print('TAREFAS', *tarefas, sep='\n')


def desfazer(tarefas, tarefas_refazer):
    print()
    # Guard clause
    if not tarefas:
        print('Não há nada para desfazer')
        print()
        return
    value = tarefas.pop()
    tarefas_refazer.append(value)
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    # Guard clause
    if not tarefas_refazer:
        print('Não há nada para desfazer')
        print()
        return

    value = tarefas_refazer.pop()
    tarefas.append(value)
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    # Guard clause
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nada')
        print()
        return

    tarefas.append(tarefa)
    listar(tarefas)


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='UTF-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'suas_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou um comando: ').lower()

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     print()
    #     continue
