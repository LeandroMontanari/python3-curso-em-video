"""
DESAFIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    novo_salario = (salario * 0.10) + salario
    print('O salário atual de R$ {:.2f} aumentou em 10% (R$ {:.2f}),'.format(salario, salario * 0.10), end=' ')
    print('totalizando R$ {:.2f}!'.format(novo_salario))
else:
    novo_salario = (salario * 0.15) + salario
    print('O salário atual de R$ {:.2f} aumentou em 15% (R$ {:.2f}),'.format(salario, salario * 0.15), end=' ')
    print('totalizando R$ {:.2f}!'.format(novo_salario))
