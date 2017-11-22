"""
NOME:
Estrutura de Repetição com Variável de Controle


EXEMPLOS DIDÁTICOS:
laço c no intervalo(1, 10):
    passo
pega

laço c no intervalo(0, 3):
    se moeda:
        pega
    passo
    pula
passo
pega


EXEMPLOS REAIS:
for c in range(1, 10):
    passo
pega

for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""
# EXEMPLO 1 - Imprime 'Oi' 6 vezes
for c in range(0, 6):
    print('Oi')
print('FIM 1')

# EXEMPLO 2 - Imprime todos os números de 1 a 6 (7 - 1), em ordem crescente
for c in range(1, 7):
    print(c)
print('FIM 2')

# EXEMPLO 3 - Imprime todos os números de 6 a 1, em ordem decrescente
for c in range(6, 0, -1):
    print(c)
print('FIM 3')

# EXEMPLO 4 - Imprime todos os números de 0 a 6, em ordem crescente, pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM 4')

# EXEMPLO 5 - Imprime todos os números de 0 a 'n' (entrada do usuário)
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM 5')

# EXEMPLO 6 - Imprime todos os números de 'i' a 'f', pulando 'p' passos a cada iteração (entradas do usuário)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM 6')

# EXEMPLO 7 - Pede para o usuário inserir um valor diferente 4 vezes e soma todos num resultado final
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))
print('FIM 7')
