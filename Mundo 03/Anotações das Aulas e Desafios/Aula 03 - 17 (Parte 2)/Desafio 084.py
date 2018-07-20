"""
DESAFIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = list()
dados = list()
nomes_maior = list()
nomes_menor = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if 'N' in continuar:
        break

cadastradas = len(pessoas)
print('-=' * 30)
print(f'Ao todo, você cadastrou {cadastradas} pessoas.')

for indice, valor in enumerate(pessoas):
    if indice == 0:
        maior = menor = valor[1]
        nomes_maior.append(valor[0])
        nomes_menor.append(valor[0])
    else:
        if valor[1] > maior:
            maior = valor[1]
            nomes_maior.clear()
            nomes_maior.append(valor[0])
        elif valor[1] == maior:
            nomes_maior.append(valor[0])

        if valor[1] < menor:
            menor = valor[1]
            nomes_menor.clear()
            nomes_menor.append(valor[0])
        elif valor[1] == menor:
            nomes_menor.append(valor[0])

print(f'O maior peso foi de {maior:.1f} kg. Peso de ', end='')
for i, n in enumerate(nomes_maior):
    if i == len(nomes_maior) - 1:
        print(f'{n}.', end='\n')
    elif i == len(nomes_maior) - 2:
        print(f'{n} e ', end='')
    else:
        print(f'{n}, ', end='')

print(f'O menor peso foi de {menor:.1f} kg. Peso de ', end='')
for i, n in enumerate(nomes_menor):
    if i == len(nomes_menor) - 1:
        print(f'{n}.', end='\n')
    elif i == len(nomes_menor) - 2:
        print(f'{n} e ', end='')
    else:
        print(f'{n}, ', end='')
