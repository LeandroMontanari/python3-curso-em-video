""" NOTA: Quando uma lista é igualada a outra no Python, ao modificar uma, a outra também é modificada junto. """
a = [2, 3, 4, 7]  # Cria uma lista "a" com alguns números inteiros
b = a  # Cria uma lista "b" idêntica à lista "a", tornando-as intrinsecamente ligadas
b[2] = 8  # Modifica o índice [2] da lista "b" para 8 (que antes era 4)

print(f'Lista A: {a}')  # Exibe a lista "a" - que teve seu índice [2] também modificado, já que é igual à lista "b"
print(f'Lista B: {b}')  # Exibe a lista "b" - que teve seu índice [2] também modificado pelo código

print('')  # Cria um espaçamento para melhor visualização

"""
Para criar duas listas com itens idênticos, porém que sejam independentes entre si, ao invés de fazer:

a = [2, 3, 4, 7]
b = a

Se faz:

a = [2, 3, 4, 7]
b = a[:]
"""

c = [1, 2, 3, 4]  # Cria uma lista "c" com alguns números inteiros
d = c[:]  # Cria uma lista "d" com os mesmos elementos da lista "c", deixando cada uma independente
d[3] = 5  # Modifica o índice [3] da lista "d" para 5 (que antes era 4)

print(f'Lista C: {c}')  # Exibe a lista "c" - que não teve seu índice [3] modificado junto com a lista "c"
print(f'Lista D: {d}')  # Exibe a lista "d" - que teve seu índice [3] modificado sozinho
