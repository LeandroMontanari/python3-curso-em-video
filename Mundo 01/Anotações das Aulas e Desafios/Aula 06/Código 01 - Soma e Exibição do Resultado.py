n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
re = n1 + n2
print('A soma entre', n1, 'e', n2, 'vale', re)  # Método 1 - Antigo, do Python 2
print('A soma entre {} e {} vale {}'.format(n1, n2, re))  # Método 2
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, re))  # Método 3
