"""
DESAFIO 070: Estatísticas em Produtos

Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
sep = '-' * 50
valortotal = 0
maisde1000 = 0
maisbarato = ''
contador = 0
anterior = 0

while True:
    print(sep)
    titulo = f'PRODUTO Nº {contador + 1}'
    print(f'{titulo:^50}')
    print(sep)
    nome = str(input('Nome: ')).strip()
    valor = float(input('Valor: R$ '))
    print(sep)

    valortotal += valor
    if valor > 1000:
        maisde1000 += 1

    if contador == 0:
        maisbarato = nome
        anterior = valor
    else:
        if valor < anterior:
            maisbarato = nome
            anterior = valor

    contador += 1
    continuar = 'I'
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer cadastrar outro produto [S/N]? '))
        continuar = continuar.strip().upper()[0].replace(' ', '')
    print(sep)
    print('')

    if continuar == 'N':
        break

print(f'O total gasto na compra foi R$ {valortotal:.2f}.', end=' ')
if maisde1000 == 0:
    print('Nenhum produto custou mais de R$ 1000.', end=' ')
elif maisde1000 == 1:
    print('1 produto custou mais de R$ 1000.', end=' ')
else:
    print(f'{maisde1000} produtos custaram mais de R$ 1000.', end=' ')
print(f'O nome do produto mais barato é {maisbarato}, que custou R$ {anterior:.2f}.')
