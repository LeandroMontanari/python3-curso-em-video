"""
DESAFIO 041: Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date
atual = date.today().year
nas = int(input('Em que ano o atleta nasceu (ex: 1990)? '))
ani = str(input('Este ano o atleta já fez aniversário? Digite S para sim ou N para não: ')).upper().strip()
if ani == 'N' or ani == 'NAO' or ani == 'NÃO':
    idade = atual - nas - 1
else:
    idade = atual - nas
if idade <= 9:
    print('O atleta de {} anos vai ficar na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('O atleta de {} anos vai ficar na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('O atleta de {} anos vai ficar na categoria JUNIOR!'.format(idade))
elif idade <= 25:
    print('O atleta de {} anos vai ficar na categoria SÊNIOR!'.format(idade))
elif idade > 25:
    print('O atleta de {} anos vai ficar na categoria MASTER!'.format(idade))
