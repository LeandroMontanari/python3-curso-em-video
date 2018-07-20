"""
DESAFIO 079: Valores Únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
lista = list()
cont = 0
msg1 = 'Digite um valor: '
msg2 = 'Valor adicionado com sucesso...'

while True:
    if cont == 0:
        lista.append(int(input(msg1)))
        print(msg2)
    else:
        num = int(input(msg1))
        if num not in lista:
            lista.append(num)
            print(msg2)
        else:
            print('Valor duplicado! Não vou adicionar...')
    cont += 1

    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Resposta inválida! Digite S para Sim ou N para Não.')
    if continuar == 'N':
        break

lista.sort()
print('-=' * 30)
print(f'Você digitou os valores {lista}')
