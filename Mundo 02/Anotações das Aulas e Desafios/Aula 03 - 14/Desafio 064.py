"""
DESAFIO 064: Tratando Vários Valores v1.0

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""
n = int(input('Digite um número qualquer (ou digite 999 para encerrar o programa): '))
if n != 999:
    numeros = 1
    soma = n
else:
    numeros = 0
    soma = 0

while n != 999:
    n = int(input('Digite um número qualquer (ou digite 999 para encerrar o programa): '))
    if n != 999:
        soma += n
        numeros += 1

if numeros == 0:
    print('Você não digitou nenhum número.')
elif numeros == 1:
    print('Você digitou somente o número {}.'.format(soma))
else:
    print('Você digitou {} números. A soma total deles é {}.'.format(numeros, soma))
