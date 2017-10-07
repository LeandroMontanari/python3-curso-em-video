n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}!'.format(m))

# Primeira Condicional - Simples
if m >= 6.0:
    print('MEUS PARABÉNS!')

# Segunda Condicional - Composta
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

# Terceira Condicional - Simplificada
print('PARABÉNS NOVAMENTE!' if m >= 6.0 else 'ESTUDE MAIS, É SÉRIO!')
