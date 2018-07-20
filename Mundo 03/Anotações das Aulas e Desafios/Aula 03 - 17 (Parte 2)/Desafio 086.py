"""
DESAFIO 086
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
