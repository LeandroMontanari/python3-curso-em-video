"""
DESAFIO 090
"""
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 7 else 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
