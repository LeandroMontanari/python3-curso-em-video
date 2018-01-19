"""
DESAFIO 043: Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
peso = float(input('Digite o seu peso em Kg (ex: 80): '))
altura = float(input('Digite o seu peso em m (ex: 1.75): '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')
