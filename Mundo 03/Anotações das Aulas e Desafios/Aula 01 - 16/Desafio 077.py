"""
DESAFIO 077
"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'

for p in palavras:
    v = ''
    for letra in p:
        if letra in vogais:
            v += ' ' + letra

    print(f'Na palavra {p.upper()} temos as vogais:{v}')
