"""
DESAFIO 065: Maior e Menor Valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""
numeros = soma = menor = maior = 0
continuar = 'S'

while continuar == 'S':
    n = int(input('Digite um número: '))
    if numeros == 0:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    numeros += 1
    soma += n

    continuar = str(input('Quer digitar outro número [S/N]? ')).upper()
    while continuar != 'S' and continuar != 'N':
        print('Resposta inválida!')
        continuar = str(input('Quer digitar outro número [S/N]? ')).upper()

media = soma / numeros
if numeros == 1:
    print('Você digitou apenas o número {}.'.format(soma))
else:
    print('Você digitou {} números. A média entre eles é {}.'.format(numeros, media))
    print('O menor número digitado foi {}. O maior número digitado foi {}.'.format(menor, maior))
