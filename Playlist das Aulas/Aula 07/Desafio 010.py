r = float(input('Quanto dinheiro em Reais você tem? '))
d = 3.27
print('\nA cotação do Dólar está a R$ {:.2f} hoje. Com R$ {:.2f}, você consegue comprar U$ {:.2f}!'.format(d, r, r / d))