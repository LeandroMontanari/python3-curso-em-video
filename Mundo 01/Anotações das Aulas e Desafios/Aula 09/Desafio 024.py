"""
DESAFIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
cidade = input('Digite o nome da cidade: ')
cl = cidade.upper().strip().split()
res = cl[0] == 'SANTO'
print('\nA cidade começa ou não com a palavra "Santo"? True significa Sim e False significa Não.')
print('Resposta: {}'.format(res))
