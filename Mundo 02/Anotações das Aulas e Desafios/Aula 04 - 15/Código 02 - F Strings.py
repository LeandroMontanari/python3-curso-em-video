"""
NOTA:
A partir da versão 3.6, o Python incluiu uma PEP onde passou a suportar F Strings, que ajudam a
simplificar a formatação de variáveis no meio de prints e textos dentro de outras váriaveis.

EXEMPLOS:

Primeiro Método - Python 2 - %:
num = 10
print('Dez é igual a %d.' % (num))

Método Anterior - Python 3 - Format:
num = 10
print('Dez é igual a {}.'.format(num))

Método Novo - Python 3.6+ - F String:
num = 10
print(f'Dez é igual a {num}.')
"""
num = 10
print('Primeiro Método - Python 2 - %:')
print('Dez é igual a %d.' % num)
print('')
print('Método Anterior - Python 3 - Format:')
print('Dez é igual a {}.'.format(num))
print('')
print('Método Novo - Python 3.6+ - F String:')
print(f'Dez é igual a {num}.')
