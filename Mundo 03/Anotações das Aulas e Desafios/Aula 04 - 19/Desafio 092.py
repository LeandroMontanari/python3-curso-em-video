"""
DESAFIO 092: Cadastro de Trabalhador em Python

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime
ano_atual = datetime.now().year
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = ano_atual - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - (ano_atual - pessoa['idade'])
print('-=' * 30)
for k, v in pessoa.items():
    if k == 'ctps':
        print(f'{k.upper()} tem o valor {v}')
    else:
        print(f'{k.capitalize()} tem o valor {v}')
