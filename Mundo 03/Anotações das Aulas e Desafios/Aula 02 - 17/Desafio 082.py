"""
DESAFIO 082
"""
lista, pares, impares = list(), list(), list()
while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Resposta inválida! Digite S para Sim ou N para Não.')

    if continuar == 'N':
        break

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')
