a = (2, 5, 4)  # Tupla "a"
b = (5, 8, 1, 2)  # Tupla "b"
c = a + b  # Cria uma nova tupla "c" contendo os elementos da tupla "a" e em seguida os da "b", sem somá-los
d = b + a  # Cria uma nova tupla "d" contendo os elementos da tupla "b" e em seguida os da "a", sem somá-los

print(a)  # Exibe (2, 5, 4)
print(b)  # Exibe (5, 8, 1, 2)
print(c)  # Exibe (2, 5, 4, 5, 8, 1, 2)
print(d)  # Exibe (5, 8, 1, 2, 2, 5, 4)
# Índices:        [0][1][2][3][4][5][6]

print(len(c))  # Exibe 7 (número de elementos de "c")

print(c.count(5))  # Exibe 2 (número de vezes que o número 5 aparece em "c")
print(c.count(4))  # Exibe 1 (número de vezes que o número 4 aparece em "c")
print(c.count(9))  # Exibe 0 (número de vezes que o número 9 aparece em "c")

print(d.index(8))  # Exibe 1 (índice que o número 8 se encontra em "d")
print(d.index(4))  # Exibe 6 (índice que o número 4 se encontra em "d")
print(d.index(2))  # Exibe 3 (índice que o primeiro número 2 se encontra em "d")

print(d.index(5))  # Exibe 0 (índice que o primeiro número 5 se encontra em "d")
print(d.index(5, 1))  # Exibe 5 (índice que o primeiro número 5 se encontra a partir do índice [1] em "d")
