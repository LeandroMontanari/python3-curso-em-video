"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

[ ] [ ] [ ] [A] [p] [r] [e] [n] [d] [a] [  ] [P ] [y ] [t ] [h ] [o ] [n ] [  ] [  ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18]
"""

frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print(frase.replace('Python', 'Android'))  # Exibe a string com um termo existente substituído por outro
print(frase.upper())  # Exibe a string toda em letras maiúsculas
print(frase.lower())  # Exibe a string toda em letras minúsculas
print(frase.capitalize())  # Exibe a string capitalizada (com apenas o primeiro caractere da frase em letra maiúscula)
print(frase.title())  # Exibe a string estilo título (com o primeiro caractere de cada palavra em letra maiúscula)
print(frase)  # A string original não foi alterada permanentemente por nenhum dos comandos utilizados acima

print('')  # Linha em branco para separar os comandos direcionados a cada string

print(frase2.strip())  # Remove todos os espaços excedentes da string
print(frase2.rstrip())  # Remove os espaços excedentes apenas do lado direito da string (inclusão do "r" no comando)
print(frase2.lstrip())  # Remove os espaços excedentes apenas do lado esquerdo da string (inclusão do "l" no comando)
print(frase2)  # Novamente, a string original não foi alterada permanentemente por nenhum dos comandos utilizados acima

print('')  # Linha em branco

frase = frase.replace('Python', 'Android')  # Desta forma sim, a string original é substituída permanentemente
print(frase)  # Exibe a string original já com as modificações feitas acima
