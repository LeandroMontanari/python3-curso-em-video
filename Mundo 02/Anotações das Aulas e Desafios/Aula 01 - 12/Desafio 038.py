n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 == n2:
    print('{} e {} são números exatamente iguais!'.format(n1, n2))
elif n1 > n2:
    print('{} é maior do que {}!'.format(n1, n2))
elif n1 < n2:
    print('{} é menor do que {}!'.format(n1, n2))
