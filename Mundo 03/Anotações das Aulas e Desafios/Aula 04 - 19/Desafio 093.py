"""
DESAFIO 093: Cadastro de Jogador de Futebol

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
qtdgols = list()
totgols = 0
div = '-=' * 30
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(partidas):
    gol = int(input(f'Quantos gols na partida {p + 1}? '))
    qtdgols.append(gol)
    totgols += gol
jogador['gols'] = qtdgols
jogador['total'] = totgols
print(div)
print(jogador)
print(div)
for k, v in jogador.items():
    print(f'O campo {k.capitalize()} tem o valor {v}.')
print(div)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    if v == 1:
        leg = 'gol'
    else:
        leg = 'gols'
    print(f'    => Na partida {i + 1}, fez {v} {leg}.')
if jogador["total"] == 1:
    leg2 = 'gol'
else:
    leg2 = 'gols'
print(f'Foi um total de {jogador["total"]} {leg2}.')
