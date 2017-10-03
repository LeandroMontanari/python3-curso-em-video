l = float(input('Digite a largura da parede, em metros: '))
a = float(input('Digite a altura da parede, em metros: '))
t = 2
m2 = l * a
r = m2 / t
print('\nA área das paredes de {:.2f}m x {:.2f}m é {:.2f}m², e será necessário comprar'.format(l, a, m2), end=' ')
print('{:.2f} litro(s) de tinta para pintar tudo!'.format(r))
