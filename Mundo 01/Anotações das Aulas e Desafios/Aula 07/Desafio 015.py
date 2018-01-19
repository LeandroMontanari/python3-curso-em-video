"""
DESAFIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
km = float(input('Qual foi a quantidade de quilômetros percorridos pelo carro alugado? '))
d = int(input('Por quantos dias ele foi alugado? '))
t = (d * 60) + (km * 0.15)
print('O carro alugado por {} dias percorreu {:.2f} quilômetros, e com isso será preciso pagar R$ {:.2f}!'.format(d, km, t))
