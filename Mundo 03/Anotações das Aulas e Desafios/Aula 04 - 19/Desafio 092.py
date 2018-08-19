"""
DESAFIO 092
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
