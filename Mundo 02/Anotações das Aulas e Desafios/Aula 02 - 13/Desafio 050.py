"""
DESAFIO 050: Soma dos Pares

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
t = 0
np = 0

for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        t += n
        np += 1

if np == 0:
    print('Você não digitou nenhum número par, portanto, o seu total é 0.')
elif np == 1:
    print('Você digitou {} número par. O seu total é {}.'.format(np, t))
else:
    print('Você digitou {} números pares. A soma total deles é {}.'.format(np, t))
