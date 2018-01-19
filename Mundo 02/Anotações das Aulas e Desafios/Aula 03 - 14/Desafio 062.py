"""
DESAFIO 062: Super Progressão Aritmética v3.0

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
print('\n10 Primeiros Termos da PA com Razão {} (Iniciando em {}):'.format(razao, primeiro))
print(primeiro, end=' → ')

while primeiro < decimo:
    primeiro += razao
    if primeiro == decimo:
        print(primeiro, end='')
    else:
        print(primeiro, end=' → ')

print('\n')
escolha = int(input('Quer ver mais quantos termos? Digite 0 para não ver mais nenhum: '))
atual = primeiro

while escolha != 0:
    ultimo = atual + (escolha - 1) * razao
    print('{}'.format(atual), end=' → ')
    while atual < ultimo + razao:
        atual += razao
        if atual > ultimo:
            print(atual, end='')
        else:
            print(atual, end=' → ')
    print('\n')
    escolha = int(input('Quer ver mais quantos termos? Digite 0 para não ver mais nenhum: '))

print('\nPrograma finalizado!')
