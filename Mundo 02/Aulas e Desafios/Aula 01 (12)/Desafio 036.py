casa = float(input('Qual é o valor da casa que você deseja comprar? R$ '))
salario = float(input('Quanto você ganha por mês? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
meses = anos * 12
prestacoes = casa / meses
minimo = salario * 30 / 100
print('Então você deseja comprar a casa no valor R$ {:.2f} em {}x de R$ {:.2f}, correto?'.format(casa, meses, prestacoes))
print('Seu salário corresponde a R$ {:.2f}, portanto, cada prestação não deve exceder o valor de R$ {:.2f} (30%).'.format(salario, minimo))
if prestacoes > minimo:
    print('Lamentamos, mas não poderemos lhe conceder o empréstimo!')
else:
    print('Sendo assim, poderemos lhe conceder o empréstimo!')