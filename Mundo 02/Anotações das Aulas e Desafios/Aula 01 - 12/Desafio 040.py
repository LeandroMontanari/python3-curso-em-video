aluno = str(input('Digite o nome do(a) aluno(a): ')).title().strip()
n1 = float(input('Digite a primeira nota de {}: '.format(aluno)))
n2 = float(input('Digite a segunda nota de {}: '.format(aluno)))
m = (n1 + n2) / 2
print('A média de {} é {}!'.format(aluno, m))
if m < 5:
    print('{} foi REPROVADO(A)!'.format(aluno))
elif 5 <= m < 6.9:
    print('{} vai ficar de RECUPERAÇÃO!'.format(aluno))
elif m > 7:
    print('{} foi APROVADO(A)!'.format(aluno))
