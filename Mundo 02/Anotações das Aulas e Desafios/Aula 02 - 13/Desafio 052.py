n = int(input('Digite um número: '))
v = True

if n < 2:
    v = False
else:
    for c in range(2, n - 1):
        if n % c == 0:
            v = False

if v:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))
