"""
DESAFIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = input('Digite seu nome completo: ')
nl = nome.upper().strip()
res = 'SILVA' in nl
print('\nVocê possui "Silva" no nome? True significa Sim e False significa Não.\nResposta: {}'.format(res))
