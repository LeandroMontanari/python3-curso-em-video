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
