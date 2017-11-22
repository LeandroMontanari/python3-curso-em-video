"""
NOME:
Estrutura de Repetição com Teste Lógico


NOTA:
Usar o for quando o laço tiver um número predefinido de repetições. Caso contrário, usar o while.


EXEMPLOS DIDÁTICOS:
enquanto não chegar na maçã:
    passo
pega

enquanto não chegar na maçã:
    se tem chão:
        passo
    se tem buraco:
        pula
    se tem moeda:
        pega
pega


EXEMPLOS REAIS:
while not chegar_na_maca:
    passo
pega

while not chegar_na_maca:
    if tem_chao:
        passo
    if tem_buraco:
        pula
    if tem_moeda:
        pega
pega
"""
# EXEMPLO 1.1 - Imprime todos os números de 1 a 10, em ordem crescente, usando o laço for
for c in range(1, 11):
    print(c)
print('FIM 1.1')

# EXEMPLO 1.2 - Faz o mesmo que o EXEMPLO 1.1, porém usando o comando while
c = 1
while c < 11:
    print(c)
    c += 1
print('FIM 1.2')

# EXEMPLO 2 - Pede para o usuário inserir um valor N vezes (indefinido), só parando quando 0 for digitado
n = 1
while n != 0:  # Flag/Condição de Parada
    n = int(input('Digite um valor: '))
print('FIM 2')

# EXEMPLO 3 - Pede para o usuário inserir um valor N vezes (indefinido) até que "r" assuma um valor diferente de 'S'
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]? ')).upper()
print('FIM 3')

# EXEMPLO 4 - Pede para o usuário inserir N valores (indefinido) e diz quantos destes são pares e quantos são ímpares
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
print('FIM 4')
