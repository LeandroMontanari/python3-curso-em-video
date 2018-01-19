"""
DESAFIO 066: Vários Números com Flag

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
s = t = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    t += 1
if t == 0:
    print('Você não digitou nenhum valor!')
elif t == 1:
    print(f'Você digitou somente 1 valor, portanto seu total é {s}!')
else:
    print(f'A soma dos {t} valores foi {s}!')
