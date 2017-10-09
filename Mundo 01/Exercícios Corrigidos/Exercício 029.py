"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar um multa de R$ {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
