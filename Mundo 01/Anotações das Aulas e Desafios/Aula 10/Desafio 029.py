"""
DESAFIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
vel = int(input('Qual velocidade o carro está? Digite um número inteiro (ex: 85): '))
multa = 7.00
total = (vel - 80) * multa
if vel > 80:
    print('O carro está a {} Km/h, sendo que a velocidade máxima permitida é 80 Km/h.'.format(vel))
    print('Nesse caso, a multa para ele é R$ {:.2f}!'.format(total))
else:
    print('O carro está a {} Km/h, portanto está dentro da velocidade máxima permitida de 80 Km/h!'.format(vel))
