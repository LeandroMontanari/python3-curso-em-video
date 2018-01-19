"""
DESAFIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
casa = float(input('Qual é o valor da casa que você deseja comprar? R$ '))
salario = float(input('Quanto você ganha por mês? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
meses = anos * 12
prestacoes = casa / meses
minimo = salario * 30 / 100
print('Então você deseja comprar uma casa no valor R$ {:.2f}'.format(casa), end=' ')
print('em {}x ({} anos) de R$ {:.2f}, correto?'.format(meses, anos, prestacoes))
print('Seu salário corresponde a R$ {:.2f}, portanto,'.format(salario), end=' ')
print('cada prestação não deve exceder o valor de R$ {:.2f} (30%).'.format(minimo))
if prestacoes > minimo:
    print('Lamentamos, mas NÃO PODEREMOS lhe conceder o empréstimo!')
else:
    print('Sendo assim, PODEREMOS lhe conceder o empréstimo!')
