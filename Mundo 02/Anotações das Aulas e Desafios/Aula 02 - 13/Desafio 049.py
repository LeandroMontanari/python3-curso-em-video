"""
DESAFIO 049: Tabuada v2.0

Refaça o DESAFIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
msg = 'Digite um número para fazer a tabuada desde o 1 até ele (ex: 10 para fazer a tabuada do 1 até o 10): '
n = int(input(msg))
print()

for c in range(1, n + 1):
    print('-' * 13)
    print('{}'.format('TABUADA DO ' + str(c)))
    print()
    for i in range(1, 10 + 1):
        print('{:<2} x {:>2} = {}'.format(c, i, c * i))
    print('-' * 13)
    print()
