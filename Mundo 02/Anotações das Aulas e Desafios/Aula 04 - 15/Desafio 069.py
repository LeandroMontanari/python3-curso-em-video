"""
DESAFIO 069: Análise de Dados do Grupo

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
sep = '-' * 50
maioresde18 = 0
homens = 0
mulheresmenos20 = 0
contador = 0
while True:
    print(sep)
    titulo = f'PESSOA Nº {contador + 1}'
    print(f'{titulo:^50}')
    print(sep)
    idade = int(input(f'Idade: '))
    sexo = 'I'
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Sexo [M/F]: '))
        sexo = sexo.strip().upper()[0].replace(' ', '')

    if idade > 18:
        maioresde18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    contador += 1
    continuar = 'I'
    print(sep)
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer cadastrar outra pessoa [S/N]? '))
        continuar = continuar.strip().upper()[0].replace(' ', '')
    print(sep)
    print('')
    if continuar == 'N':
        break

if contador == 1:
    print('Você cadastrou somente 1 pessoa. Deste número,', end=' ')
else:
    print(f'Você cadastrou {contador} pessoas no total. Deste número,', end=' ')

if maioresde18 == 0:
    print('nenhuma tem mais de 18 anos,', end=' ')
elif maioresde18 == 1:
    print('1 tem mais de 18 anos,', end=' ')
else:
    print(f'{maioresde18} têm mais de 18 anos,', end=' ')

if homens == 0:
    print('nenhum é homem,', end=' ')
elif homens == 1:
    print('1 é homem,', end=' ')
else:
    print(f'{homens} são homens,', end=' ')

if mulheresmenos20 == 0:
    print('e nenhuma mulher tem menos de 20 anos.')
elif mulheresmenos20 == 1:
    print('e 1 mulher tem menos de 20 anos.')
else:
    print(f'e {mulheresmenos20} mulheres têm menos de 20 anos.')
