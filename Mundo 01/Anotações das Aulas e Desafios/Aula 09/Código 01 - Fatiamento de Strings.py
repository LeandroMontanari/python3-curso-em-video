"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

NOTA: Para o Python, por exemplo, "V" maiúsculo é diferente de "v" minúsculo.

Exemplos de Estruturas de Fatiamento:
variavel[IN:FI:SA]
variavel[IN:]
variavel[:FI]
variavel[::SA]
variavel[IN::SA]
Onde "IN" é o índice inicial, "FI" é o índice final e "SA" é a quantidade de caracteres a saltar em cada passo
"""

frase = 'Curso em Vídeo Python'

print(frase)  # Exibe a frase inteira
print(frase[9])  # Exibe o caractere de índice [9] na frase, no caso, a letra "V"
print(frase[9:13])  # Exibe desde o caractere de índice [9] até o [13], porém excluindo este último, ficando "Víde"
print(frase[9:14])  # Exibe desde o caractere de índice [9] até o [14], porém excluindo este último, ficando "Vídeo"
print(frase[9:21])  # Apesar de o índice [21] não existir na frase, como o último é excluído, fica "Vídeo Python"
print(frase[9:21:2])  # Exibe do índice [9] ao [21], pulando de 2 em 2, ficando "VdoPto"
print(frase[:5])  # Exibe do índice inicial (0, no caso) até o [5] (lembrando: excluindo este), ficando "Curso"
print(frase[15:])  # Exibe do índice [15] até o final (21, no caso), ficando "Python"
print(frase[9::3])  # Exibe do índice [9] até o final (21, no caso), pulando de 3 em 3, ficando "VePh"
print(frase[::2])  # Exibe do índice inicial [0] até o final (21, no caso), pulando de 2 em 2, ficando "Croe íe yhn"
