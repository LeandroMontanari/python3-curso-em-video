"""
EXERCÍCIO 086: Matriz em Python

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
