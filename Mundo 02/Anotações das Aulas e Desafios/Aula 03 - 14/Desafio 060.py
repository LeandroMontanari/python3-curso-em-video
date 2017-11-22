"""
# Feito com for
numero = int(input('Digite um número para descobrir seu fatorial: '))
copia = numero
resultado = numero
add = ''

for n in range(numero):
    if copia != numero:
        resultado *= copia
    add += str(copia)
    if copia != 1:
        add += ' x '
    copia -= 1

print('{}! = {} = {}'.format(numero, add, resultado))
"""
# Feito com while
numero = int(input('Digite um número para descobrir seu fatorial: '))
copia = numero
resultado = numero
add = ''

while copia > 0:
    if copia != numero:
        resultado *= copia
    add += str(copia)
    if copia != 1:
        add += ' x '
    copia -= 1

print('{}! = {} = {}'.format(numero, add, resultado))
