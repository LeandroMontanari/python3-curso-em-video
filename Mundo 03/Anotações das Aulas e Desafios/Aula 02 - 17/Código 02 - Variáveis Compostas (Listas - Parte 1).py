valores = list(range(4, 11))  # Cria uma lista "valores" com os números de 4 até 10 (o último número, 11, é ignorado)
print(valores)  # Exibe [4, 5, 6, 7, 8, 9, 10]
# Índices:              [0][1][2][3][4][5][6]

valores2 = [8, 2, 5, 4, 9, 3, 0]  # Cria uma lista "valores2" com os números inseridos entre colchetes
print(valores2)  # Exibe [8, 2, 5, 4, 9, 3, 0]
# Índices:              [0][1][2][3][4][5][6]

valores2.sort()  # Organiza os números presentes na lista "valores2" em ordem crescente
print(valores2)  # Exibe [0, 2, 3, 4, 5, 8, 9] (com os números já reordenados pelo comando anterior)
# Índices:               [0][1][2][3][4][5][6]

valores2.sort(reverse=True)  # Organiza os números presentes na lista "valores2" em ordem decrescente
print(valores2)  # Exibe [9, 8, 5, 4, 3, 2, 0] (com os números também já reordenados pelo comando anterior)
# Índices:               [0][1][2][3][4][5][6]

n = len(valores2)  # Atribui à variável "n" o valor correspondente à quantidade de itens presentes na lista "valores2"
print(n)  # Exibe 7 (7 itens, correspondentes aos índices de [0] até [6])
