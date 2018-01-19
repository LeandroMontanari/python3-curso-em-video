"""
DESAFIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
n = int(input('Digite o valor em metros: '))
cm = n * 100
mm = n * 1000
print('{} metro(s) equivale(m) a {} centímetros ou a {} milímetros.'.format(n, cm, mm))
