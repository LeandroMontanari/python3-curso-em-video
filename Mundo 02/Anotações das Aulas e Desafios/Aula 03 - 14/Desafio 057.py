sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Digite M para sexo MASCULINO ou F para sexo FEMININO.')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Você do sexo MASCULINO!')
elif sexo == 'F':
    print('Você é do sexo FEMININO!')
