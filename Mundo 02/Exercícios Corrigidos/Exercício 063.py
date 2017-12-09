"""
Sequencia de Fibonacci
"""

fibonacci = int(input('Quantos numeros da sequência de Fibonacci '))

v1, v2 = -1, 1

v3 = v1 + v2
count = 1

while count <= fibonacci:
    v3 = v1 + v2
    v1 = v2
    v2 =v3
    print(f'{v3}', end='')
    count += 1
