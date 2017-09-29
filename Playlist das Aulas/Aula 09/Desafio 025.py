nome = input('Digite seu nome completo: ')
nl = nome.upper().strip()
res = 'SILVA' in nl
print('\nVocê possui "Silva" no nome? True significa Sim e False significa Não.\nResposta: {}'.format(res))