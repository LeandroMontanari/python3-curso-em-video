"""
Gerador de PA
com while
"""
print('Gerador de PA')
print('-= ' * 10)
primeiro = int(input('Primeiro termo: '))#pega o primeiro termo
razao = int(input('A Razão: '))#e sua razão
termo = primeiro
count = 1
while count <= 10:#os 10 primeiros termos
    print('{} → '.format(termo), end=' ')
    termo += razao#esse ele acrescenta o a razão ao termo 'Termo  = termo + razao'
    count +=1
print('FIM :)')#finaliza o código
