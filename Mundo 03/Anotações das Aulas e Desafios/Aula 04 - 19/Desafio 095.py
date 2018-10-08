"""
DESAFIO 095: Aprimorando os Dicionários

Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
div = '-' * 35
div2 = '-' * 44
jogador = dict()
jogadores = list()
qtdgols = list()
totgols = 0
while True:
    print(div)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(partidas):
        gol = int(input(f'Quantos gols na partida {p + 1}? '))
        qtdgols.append(gol)
        totgols += gol
    jogador['gols'] = qtdgols[:]
    jogador['total'] = totgols
    jogadores.append(jogador.copy())
    totgols = 0
    qtdgols.clear()
    continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
print(div2)
print(f'{" CÓD":<5}', end=' ')
print(f'{"NOME":<15}', end=' ')
print(f'{"GOLS":<15}', end=' ')
print(f'{"TOTAL":<7}', end=' ')
print()
print(div2)
for i, j in enumerate(jogadores):
    print(f'{i + 1:>4}', end=' ')
    print(f' {j["nome"]:<15}', end=' ')
    print(f'{str(j["gols"]):<15}', end=' ')
    print(f'{j["total"]:<7}', end=' ')
    print()
print(div2)
while True:
    mostrar = int(input('Mostrar dados de qual jogador (digite 999 para encerrar o programa)? '))
    if mostrar == 999:
        break
    elif mostrar > len(jogadores) or mostrar <= 0:
        print(f'ERRO! Não existe jogador com código {mostrar}! Tente novamente.')
    else:
        print(f'-- Levantamento do Jogador {jogadores[mostrar - 1]["nome"]}:')
        for i, j in enumerate(jogadores[mostrar - 1]["gols"]):
            if j == 1:
                leg_gols = 'gol'
            else:
                leg_gols = 'gols'
            print(f'   No jogo {i + 1} fez {j} {leg_gols}.')
    print(div2)
print('<< VOLTE SEMPRE >>')
