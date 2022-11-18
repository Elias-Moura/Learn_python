# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está  e as pastas abaixo dele
# Ele não reconhce pastas e módlos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

print('Este módulo se chama', __name__)

"""
Para importar um módulo seu que não está no mesmo local do atual. 
Utilize:

import sys

sys.path.append('caminho do arquivo aqui')

após isso deve funcionar.
"""


'''
Como recarregar um módulo?

import importlib

importlib.reload(módulo_aqui)
'''

"""
Como importar módulos de um pacote python? (package)

------

from packege.nome_do_módulo import nome_do_que_você_quer_importar

Dessa forma você não tem o name_space e pode chamar somente o que você importou.

-----

from packege import modulo

Dessa forma você terá o name_space modulo e precisará usar "modulo.método_que_você_quer"

-----

import package.modulo

Dessa forma voce terá o name_space "package.modulo.método_que_você_quer"

"""

"""
Todo pacote python pode ter um arquivo chamado __init__.py

Lá podemos colocar um from modulo(que está dentro do pacote) import *

Pois o __init__ sempre será execuado na impotação do pacote. (se comportando como se fosse um módulo).

Dessa maneira, simplificamos a importação de módulos.

"""