"""
Ordem de Precedência (O que é levado em conta primeiro no código do Python):
#1 () - Parênteses
#2 ** - Potência/Exponenciação
#3 *, /, // e % - Multiplicação, Divisão, Divisão Inteira e Resto da Divisão (O que aparecer primeiro no código, executa primeiro)
#4 + e - - Adição e Subtração (O que aparecer primeiro no código, executa primeiro)
"""
5 + 3 * 2 == 11 # Primeiro se resolve a Multiplicação, depois a Adição
3 * 5 + 4 ** 2 == 31 # Primeiro se resolve a Exponenciação, depois a Multiplicação, e por fim a Adição
3 * (5 + 4) ** 2 == 243 # Primeiro se reolve o que tem dentro dos Parênteses, depois a Exponenciação, e por fim a Multiplicação