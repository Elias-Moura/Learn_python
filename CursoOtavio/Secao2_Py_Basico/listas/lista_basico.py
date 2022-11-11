"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

palavras_pesadelo = [
    'Aeropiesotermoterápico',
    'Acrocefalossindactilia',
    'Anticonstitucionalmente',
    'Anticonstitucionalismo',
    'Celiossalpingectômico',
    'Cineangiocoronariográfico',
    'Coledocoduodenostômico',
    'Coronografopolarímetro',
    'Cristaloluminescência',
    'Diacetilenodicarbonato',
    'Estereofotogramétrico',
    'Espectrocolorimétrico',
    'Fotocromometalografia',
    'Fotocromometalográfico',
    'Hexanitrodifenilamina',
    'Hidropneumopericárdio',
    'Histerossalpingectomia',
    'Histerossalpingografia',
    'Histerossalpingográfico',
    'Interconfessionalismo',
    'Inconstitucionalidade',
    'Inconstitucionalissimamente',
    'Inconstitucionalmente',
    'Interdisciplinaridade',
    'Meningoencefalomielite',
    'Multidisciplinaridade',
    'Oftalmotorrinolaringologista',
    'Otorrinolaringologista',
    'Parassimpaticomimético',
    'Pneumartrorradiografia',
    'Preterintencionalidade',
    'Supertuberculinização',
    'Transdisciplinaridade',
    'Traquelangulescapular',
    'Traquelatloidoccipital',
    'Ureteropielonefrítico',
    'Ureteropieloneostômico',

]

print(len(palavras_pesadelo))

for i, palavra in enumerate(palavras_pesadelo):
    palavras_pesadelo[i] = palavra.lower()

with open('text.txt', "w", encoding='UTF-8') as f:
    f.write(str(palavras_pesadelo))
