from time import sleep
print('Contagem regressiva para estourar os fogos de artifício:')
for c in range(10, 0 - 1, -1):
    sleep(1)
    if c != 0:
        print('{}...'.format(c))
    else:
        print('BOOOM!')
