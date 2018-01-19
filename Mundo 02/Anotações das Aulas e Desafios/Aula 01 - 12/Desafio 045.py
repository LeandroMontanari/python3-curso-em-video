"""
DESAFIO 045: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
adv = choice(opcoes)
print('Digite qual você quer jogar!')
jogador = str(input('PEDRA, PAPEL ou TESOURA? ')).lower().strip()
if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    print('Você jogou {} e eu joguei {}.'.format(jogador.upper(), adv.upper()))
    if adv == jogador:
        print('Nós empatamos!')
    elif adv == 'pedra' and jogador == 'papel':
        print('Você ganhou!')
    elif adv == 'pedra' and jogador == 'tesoura':
        print('Eu ganhei!')
    elif adv == 'papel' and jogador == 'pedra':
        print('Eu ganhei!')
    elif adv == 'papel' and jogador == 'tesoura':
        print('Você ganhou!')
    elif adv == 'tesoura' and jogador == 'pedra':
        print('Você ganhou!')
    elif adv == 'tesoura' and jogador == 'papel':
        print('Eu ganhei!')
    else:
        print('Erro!')
else:
    print('Jogada inválida! Digite PEDRA, PAPEL ou TESOURA!')
