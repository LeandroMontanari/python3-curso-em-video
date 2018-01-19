"""
DESAFIO 061: Progressão Aritmética v2.0

Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(razao, primeiro))
print(primeiro, end=' → ')

while primeiro < decimo:
    primeiro += razao
    if primeiro == decimo:
        print(primeiro, end='')
    else:
        print(primeiro, end=' → ')
