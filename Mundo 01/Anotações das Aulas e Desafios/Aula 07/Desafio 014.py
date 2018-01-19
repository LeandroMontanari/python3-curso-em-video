"""
DESAFIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
c = float(input('Digite a temperatura em ºC: '))
f = (9 * (c / 5)) + 32
print('{:.1f}ºC é igual a {:.1f}ºF!'.format(c, f))
