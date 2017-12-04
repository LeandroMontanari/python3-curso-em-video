"""
Programa para calcular o factorial de um número
"""
n = int(input('Digite um número para calcular o seu Factorial: '))#número digitado pelo usuário
c = n #contador regressivo
f = 1 #contador do factorial

while c > 0:
    """
    Nesta etapa pegamos o valor do contador
    juntamente com o número digitado do usuário
    para poder fazer o cáculo do factorial.
    """
    f *= c #contador do factorial
    c -= 1 #contador regressivo
print(f'O fatorial de {n} é {f}')#Imprime o factorial do resultado
