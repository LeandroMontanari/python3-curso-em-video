"""
DESAFIO 094: Unindo Dicionários e Listas

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
pessoa = dict()
pessoas = list()
media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
print('-=' * 30)
if len(pessoas) == 1:
    leg1 = 'pessoa'
else:
    leg1 = 'pessoas'
print(f'- O grupo tem {len(pessoas)} {leg1}.')
print(f'- A média de idade é de {media / len(pessoas):.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for pes in pessoas:
    if pes['idade'] > media / len(pessoas):
        print()
        for k, v in pes.items():
            print(f'{k.capitalize()} = {v};', end=' ')
print()
print()
print('<< ENCERRADO >>')
