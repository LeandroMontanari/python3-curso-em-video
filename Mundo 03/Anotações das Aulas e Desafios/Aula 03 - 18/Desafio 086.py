"""
DESAFIO 086: Matriz em Python

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [
    [],
    [],
    []
]
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(n)

print('-=' * 30)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print()
