"""
DESAFIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
ano = int(input('Digite um ano (ex: 1997): '))
tam = len(str(ano))  # Atribui à variável "tam" a quantidade de caracteres que tem o ano digitado
if ano % 4 == 0:  # Verifica se o resto da divisão por 4 do ano digitado é igual a 0
    if str(ano)[tam - 1] == '0':  # Verifica se o último caractere do ano digitado é 0
        if str(ano)[tam - 2] == '0':  # Verifica se o penúltimo caractere do ano digitado é 0
            if ano % 400 == 0:  # Verifica se o resto da divisão por 400 do ano digitado é igual a 0
                print('{} é um ano bissexto!'.format(ano))
            else:
                print('{} não é um ano bissexto!'.format(ano))
        else:
            print('{} é um ano bissexto!'.format(ano))
    else:
        print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))
