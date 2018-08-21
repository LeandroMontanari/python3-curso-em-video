"""
DESAFIO 089: Boletim com Listas Compostas

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
alunos = list()
div1, div2, div3 = '-=' * 13, '-' * 26, '-' * 35

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    if 'N' in continuar:
        break

print(div1)
print(f'{" Nº":<5}', end='')
print(f'{"NOME":<14}', end='')
print(f'{"MÉDIA":>6}', end='\n')

print(div2)
for a in range(len(alunos)):
    print(f' {a:<4}', end='')
    print(f'{alunos[a][0]:<14}', end='')
    print(f'{alunos[a][2]:>6.1f}', end='\n')
print(div3)

while True:
    mostrar = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if mostrar == 999:
        break
    else:
        if mostrar < 0 or mostrar > len(alunos) - 1:
            print(f'Número inexistente! Digite o número correspondente ao aluno, entre 0 e {len(alunos) - 1}.')
        else:
            print(f'As notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}')
        print(div3)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
