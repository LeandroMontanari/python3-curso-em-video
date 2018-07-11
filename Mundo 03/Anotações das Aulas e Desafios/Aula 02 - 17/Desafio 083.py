"""
DESAFIO 083: Validando Expressões Matemáticas

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
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
