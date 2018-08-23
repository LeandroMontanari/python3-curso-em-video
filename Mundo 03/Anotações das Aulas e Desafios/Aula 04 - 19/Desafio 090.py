"""
DESAFIO 090: Dicionário em Python

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 7 else 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
