"""
NOME:
Estrutura de Repetição Infinita


EXEMPLO DIDÁTICO:
enquanto Verdadeiro:
    se tem chão:
        passo
    se tem buraco:
        pula
    se tem moeda:
        pega
    se tem troféu:
        pula
        interrompe
pega


EXEMPLO REAL:
while True:
    if tem_chao:
        passo
    if tem_buraco:
        pula
    if tem_moeda:
        pega
    if tem_trofeu:
        pula
        break
pega
"""
# EXEMPLO 1 - Imprime todos os números de 1 a 10, em ordem crescente, usando o comando while
cont = 1
while cont <= 10:
    print(cont, '→ ', end='')
    cont += 1
print('FIM 1')

# EXEMPLO 2 - Pede para o usuário digitar um número infinitas vezes, só parando quando ele digitar 999 (flag)
n = 0
while n != 999:
    n = int(input('Digite um número: '))
print('FIM 2')

# EXEMPLO 3 - Faz o mesmo que o exemplo acima, porém também soma os números digitados, inclusive o 999 (flag)
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}.'.format(s))
print('FIM 3')

# EXEMPLO 4 - Faz o mesmo que o exemplo acima com um loop infinito, porém não soma junto o 999 (flag)
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format(s))
print('FIM 4')
