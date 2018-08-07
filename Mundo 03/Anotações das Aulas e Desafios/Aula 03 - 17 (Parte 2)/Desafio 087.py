"""
DESAFIO 087: Mais Sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""
matriz = [
    [],
    [],
    []
]

pares = terceira = maior = 0

for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(n)

print('-=' * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if coluna == 3 - 1:
            terceira += matriz[linha][coluna]
        if linha == 2 - 1:
            if coluna == 0:
                maior = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maior:
                    maior = matriz[linha][coluna]
    print()
print('-=' * 30)

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
