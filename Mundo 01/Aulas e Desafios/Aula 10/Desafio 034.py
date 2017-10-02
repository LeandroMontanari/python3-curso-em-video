salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    novo_salario = (salario * 0.10) + salario
    print('O salário atual de R$ {:.2f} aumentou em 10% (R$ {:.2f}), totalizando R$ {:.2f}!'.format(salario, salario * 0.10, novo_salario))
else:
    novo_salario = (salario * 0.15) + salario
    print('O salário atual de R$ {:.2f} aumentou em 15% (R$ {:.2f}), totalizando R$ {:.2f}!'.format(salario, salario * 0.15, novo_salario))