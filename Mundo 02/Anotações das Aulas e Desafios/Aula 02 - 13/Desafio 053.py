frase = str(input('Digite uma frase: ')).replace('"', '').replace("'", "").capitalize()
frase_formatada = frase.lower().strip().replace(' ', '')
frase_final = frase_formatada

substituicoes = {
    'á': 'a',
    'à': 'a',
    'ã': 'a',
    'â': 'a',
    'é': 'e',
    'ê': 'e',
    'í': 'i',
    'ó': 'o',
    'õ': 'o',
    'ô': 'o',
    'ú': 'u',
    'ü': 'u',
    'ç': 'c',
    '"': '',
    "'": "",
    ',': '',
    '.': '',
    '!': '',
    ';': '',
    ':': '',
    '?': '',
    '-': '',
    '_': '',
    '(': '',
    ')': '',
    'º': '',
    '<': '',
    '>': '',
    '@': '',
    '#': '',
    '$': '',
    '%': '',
    '*': '',
    '+': '',
    '=': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    '&': '',
    '/': '',
    '\\': ''
    }

for caractere in substituicoes:
    frase_final = frase_final.replace(caractere, substituicoes[caractere])

frase_final_invertida = frase_final[::-1]

if frase_final == frase_final_invertida:
    print('\n"{}" é um palíndromo.'.format(frase))
else:
    print('\n"{}" não é um palíndromo.'.format(frase))
