"""
DESAFIO 053: Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
acentos = {'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'é': 'e', 'ê': 'e', 'í': 'i',
           'ó': 'o', 'õ': 'o', 'ô': 'o', 'ú': 'u', 'ü': 'u', 'ç': 'c', "'": ""}

outros = '"´`~^¨,.!;:?-_()[]{}<>ºªº¹²³@#$£¢§¬%*+%=&/\\'

frase = str(input('Digite uma frase: ')).replace('"', '').replace("'", "").capitalize()
frase_final = frase.lower().strip().replace(' ', '')

for caractere in acentos:
    frase_final = frase_final.replace(caractere, acentos[caractere])

for caractere_especial in outros:
    frase_final = frase_final.replace(caractere_especial, '')

frase_final_invertida = frase_final[::-1]

if frase_final == frase_final_invertida:
    print('\n"{}" é um palíndromo.'.format(frase))
else:
    print('\n"{}" não é um palíndromo.'.format(frase))
