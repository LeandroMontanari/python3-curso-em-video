"""
DESAFIO 088
"""
from random import randint
from time import sleep

sorteio, megasena = list(), list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 4, end=' ')
print(f'SORTEANDO {jogos} JOGOS', end=' ')
print('-=' * 4)

for j in range(jogos):
    b1, b2, b3 = randint(1, 60), randint(1, 60), randint(1, 60)
    b4, b5, b6 = randint(1, 60), randint(1, 60), randint(1, 60)
    while b2 == b1:
        b2 = randint(1, 60)
    while b3 == b2 or b3 == b1:
        b3 = randint(1, 60)
    while b4 == b3 or b4 == b2 or b4 == b1:
        b4 = randint(1, 60)
    while b5 == b4 or b5 == b3 or b5 == b2 or b5 == b1:
        b5 = randint(1, 60)
    while b6 == b5 or b6 == b4 or b6 == b3 or b6 == b2 or b6 == b1:
        b6 = randint(1, 60)
    sorteio.append(b1)
    sorteio.append(b2)
    sorteio.append(b3)
    sorteio.append(b4)
    sorteio.append(b5)
    sorteio.append(b6)
    sorteio.sort()
    megasena.append(sorteio[:])
    sorteio.clear()
    print(f'Jogo {j + 1}: {megasena[j]}')
    sleep(1)

print('-=' * 5, end=' ')
print('< BOA SORTE! >', end=' ')
print('-=' * 5)
