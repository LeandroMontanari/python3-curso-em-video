"""
Em Python, existem 3 tipos de Variáveis Compostas:
- Tuplas
- Listas
- Dicionários

Exemplo de Variável Simples:
lanche = 'Hambúrguer'

Exemplo de Tupla (Variável Composta):
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
Índices:      [0]        [1]      [2]      [3]

NOTA 1: As Tuplas são IMUTÁVEIS!

NOTA 2: Tuplas são identificadas por "()" (parênteses). Nas versões mais atuais do Python
nem é necessário colocar entre "()", mas facilita para melhor entendimento do código.
"""
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')  # Tupla "lanche"

print(lanche)  # Exibe ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# lanche[1] = 'Refrigerante' -> Comando impossível, pois tuplas são imutáveis

print(lanche[0])  # Exibe Hambúrguer
print(lanche[1])  # Exibe Suco
print(lanche[2])  # Exibe Pizza
print(lanche[3])  # Exibe Pudim

print(lanche[0:2])  # Exibe ('Hambúrguer', 'Suco')
print(lanche[1:3])  # Exibe ('Suco', 'Pizza')
print(lanche[1:])  # Exibe ('Suco', 'Pizza', 'Pudim')
print(lanche[:2])  # Exibe ('Hambúrguer', 'Suco')
print(lanche[-1])  # Exibe Pudim
print(lanche[-2])  # Exibe Pizza
print(lanche[-3:])  # Exibe ('Suco', 'Pizza', 'Pudim')

print(len(lanche))  # Exibe 4 (número de elementos de "lanche")

print(sorted(lanche))  # Exibe os elementos da tupla "lanche" em ordem alfabética, na forma de lista

# For 1 - Somente o elemento
for comida in lanche:  # Para cada "comida" em "lanche"...
    print(f'{comida}')  # Exibe a "comida" atual

# For 2.1 - Elemento e posição com o comando "range"
for cont in range(0, len(lanche)):  # Para cada número "cont" de 0 ao número de elementos em "lanche"...
    print(f'{lanche[cont]} na posição {cont}')  # Exibe o elemento na posição "cont" de "lanche" e o valor de "cont"

# For 2.2 - Elemento e posição com o comando "enumerate"
for pos, quecomida in enumerate(lanche):  # Para cada posição "pos" e elemento "quecomida" em "lanche"...
    print(f'{quecomida} na posição {pos}')  # Exibe o elemento "quecomida" e a posição "pos" atuais
