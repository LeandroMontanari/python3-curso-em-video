from random import randint
from time import sleep
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('Ranking dos jogadores:')
contador = 1
for item in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {contador}º lugar: {item} com {jogadores[item]}')
    contador += 1
    sleep(1)
