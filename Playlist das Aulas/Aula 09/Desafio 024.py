cidade = input('Digite o nome da cidade: ')
cl = cidade.upper().strip().split()
res = cl[0] == 'SANTO'
print('\nA cidade começa ou não com a palavra "Santo"? True significa Sim e False significa Não.\nResposta: {}'.format(res))