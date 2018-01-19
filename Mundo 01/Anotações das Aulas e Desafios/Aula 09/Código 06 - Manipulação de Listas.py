frase = 'Curso em Vídeo Python'
frase_dividida = frase.split()  # Atribui à variável "frase_dividida" a lista de palavras contidas em "frase"
print(frase_dividida[0])  # Exibe a primeira palavra na lista criada acima
print(frase_dividida[2])  # Exibe a terceira palavra na lista
print(frase_dividida[3][0])  # Exibe a primeira letra da quarta palavra na lista
print(frase_dividida[3][0:3])  # Exibe da primeira até a terceira letra da quarta palavra na lista
print(frase_dividida[0][::2])  # Exibe da primeira até a última letra da primeira palavra na lista, pulando de 2 em 2
