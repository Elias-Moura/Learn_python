'''
Operador ternário em Python # Economisa linhas mas é mais confuso de início.
'''

logged_user = False

# printa 'Usuário logado' if logged_user é Vdd else printa 'usuário precisa logar.'
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)

#  4 linhas feitas em apenas uma linha ^

# if logged_user: # logged_user == True
#     msg = 'Usuário Logado.'
# else:
#     msg = 'Usuário precisa logar.'
#
# print(msg)

# Exemplo 2

idade = input('Digite a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

print(msg)
# if idade >= 18:
#     print('Pode acessar.')
# else:
#     print('Não pode acessar.')
