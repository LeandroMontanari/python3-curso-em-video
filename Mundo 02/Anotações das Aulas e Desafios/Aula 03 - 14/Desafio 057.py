sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Valor inválido! Digite M para sexo MASCULINO ou F para sexo FEMININO.')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
if sexo == 'M':
    print('A pessoa é do sexo MASCULINO!')
elif sexo == 'F':
    print('A pessoa é do sexo FEMININO!')
