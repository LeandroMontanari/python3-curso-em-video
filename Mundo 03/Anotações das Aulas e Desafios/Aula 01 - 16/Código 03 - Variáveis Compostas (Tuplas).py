# Tuplas aceitam vários tipos de dados, não necessariamente do mesmo tipo.
pessoa = ('Gustavo', 39, 'M', 99.88)  # Tupla "pessoa" com dados str, int, str e float, respectivamente

print(pessoa)  # Exibe ('Gustavo', 39, 'M', 99.88)

del(pessoa)  # Deleta a tupla "pessoa" inteira
# del(pessoa[0]) -> Comando impossível, pois não se pode deletar um único elemento da tupla
