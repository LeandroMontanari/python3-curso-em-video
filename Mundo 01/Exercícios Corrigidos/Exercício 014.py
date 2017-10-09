"""
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
