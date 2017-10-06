from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))
