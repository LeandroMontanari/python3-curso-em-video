"""
DESAFIO 067: Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
sep = '-' * 20
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print(sep)
    for n in range(1, 10 + 1):
        print(f'{tabuada} x {n:2} = {tabuada * n}')
    print(sep)
print(sep)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
