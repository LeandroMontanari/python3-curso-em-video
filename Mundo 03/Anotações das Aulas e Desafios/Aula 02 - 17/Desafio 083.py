"""
DESAFIO 083
"""
par1, par2 = list(), list()
expressao = str(input('Digite a expressão: '))
for caractere in expressao:
    if '(' in caractere:
        par1.append(caractere)
    if ')' in caractere:
        par2.append(caractere)
if len(par1) == len(par2):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
