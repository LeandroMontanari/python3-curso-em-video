"""
DESAFIO 081: Extraindo Dados de uma Lista

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()

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

lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
