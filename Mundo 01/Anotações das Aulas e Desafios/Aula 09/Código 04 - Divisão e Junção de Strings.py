"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]
"""

frase = 'Curso em Vídeo Python'
frase_separada = frase.split()  # Separa cada palavra da string em uma lista; os índices são refeitos
print(frase_separada)  # Exibe a lista de palavras separadas

"""
ÍNDICES REFEITOS

[C] [u] [r] [s] [o]   [e] [m]   [V] [í] [d] [e] [o]   [P] [y] [t] [h] [o] [n]
[0] [1] [2] [3] [4]   [0] [1]   [0] [1] [2] [3] [4]   [0] [1] [2] [3] [4] [5]
[        0        ]   [  1  ]   [        2        ]   [          3          ]
"""

frase_junta_hifen = '-'.join(frase_separada)  # Junta as palavras separadas na lista com o caractere "-" como divisor
print(frase_junta_hifen)   # Exibe a string junta novamente, desta vez com "-" no lugar dos espaços

frase_junta_espaco = ' '.join(frase_separada) # Junta as palavras separadas na lista usando um espaço como divisor
print(frase_junta_espaco)  # Exibe a string junta novamente, com o espaço sendo o divisor, como na original
