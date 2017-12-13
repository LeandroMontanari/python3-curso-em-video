"""
Tratando números digitados
"""
soma = c = 0 #aqui um jeito rápido de se escrever variáveis com o mesmo valor
n = int(input('Digite um número [999 para sair]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para sair]: '))
    """o no fica ao final do código caso fique o n seja declarado 999,
     estando no fim do while não será adicionado n variável soma"""
print(f'O total de números digitados foram {c} e a soma deles foram {soma}')
