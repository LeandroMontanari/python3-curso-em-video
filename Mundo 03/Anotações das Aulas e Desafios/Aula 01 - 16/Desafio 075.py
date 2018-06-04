"""
DESAFIO 075: Análise de Dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
nove = numeros.count(9)
pares = 0
qpares = ''

if numeros.count(3) > 0:
    tres = numeros.index(3)
    frase = f'O valor 3 apareceu na {tres + 1}ª posição.'
else:
    frase = 'O valor 3 não foi digitado em nenhuma posição.'

if nove == 1:
    desc = 'vez'
else:
    desc = 'vezes'

for n in numeros:
    if n % 2 == 0:
        pares += 1
        qpares += ' ' + str(n)

if pares > 0:
    frase_pares = f'Os valores pares digitados foram:{qpares}'
else:
    frase_pares = 'Nenhum valor par foi digitado.'

print('')
print(f'Você digitou os valores: {numeros}')
print('')
print(f'O valor 9 apareceu {nove} {desc}.')
print(frase)
print(frase_pares)
