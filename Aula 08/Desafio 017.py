from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
r = hypot(c1, c2)
print('\nO comprimento da hipotenusa é {}!'.format(r))