nome = input('Digite seu nome completo: ').strip().split()
qtd = len(nome)
print('\nSeu primeiro nome é {} e seu último nome é {}!'.format(nome[0], nome[qtd-1]))