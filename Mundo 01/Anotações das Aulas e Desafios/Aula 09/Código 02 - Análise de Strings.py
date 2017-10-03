"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]
"""

frase = 'Curso em Vídeo Python'

print(len(frase))  # Exibe a quantidade de caracteres de uma string (no caso, 21)
print(frase.count('o'))
""" Exibe a quantidade de vezes que o caractere entre parênteses (no caso, "o" minúsculo)
aparece na string (no caso, 3) """
print(frase.count('o', 0, 13))
""" Idem ao caso acima, porém aqui foi incluído um fatiamento do índice [0] ao [13]-1, exibindo "1" """
print(frase.count('o', 0, 14))  # Idem ao caso acima, porém aqui o índice final ficou sendo [14]-1, exibindo "2"
print(frase.find('deo'))  # Exibe o índice inicial (11, no caso) do que está entre parênteses
print(frase.find('Android'))  # Quando se procura na string algo que não está presente, o valor exibido é "-1"
print('Curso' in frase)  # Verifica se o que está entre aspas está presente na string, e se sim, exibe "True"
