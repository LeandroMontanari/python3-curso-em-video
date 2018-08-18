teste = list()  # Cria uma nova lista vazia "teste"
teste.append('Gustavo')  # Adiciona a string 'Gustavo' ao final da lista "teste"
teste.append(40)  # Adiciona o número inteiro 40 ao final da lista "teste"

galera = list()  # Cria uma nova lista vazia "galera"
galera.append(teste)  # Adiciona a própria lista "teste" (e não uma cópia) à lista composta "galera"

print(teste)  # Exibe ['Gustavo', 40]
print(galera)  # Exibe [['Gustavo', 40]]

teste[0] = 'Maria'  # Muda o item [0] da lista "teste", de 'Gustavo' para 'Maria'
teste[1] = 22  # Muda o item [1] da lista "teste", de 40 para 22

print(teste)  # Exibe ['Maria', 22]

galera.append(teste)  # Adiciona novamente a própria lista "teste" (já modificada) à lista composta "galera"
print(galera)  # Exibe [['Maria', 22], ['Maria', 22]] (e não [['Gustavo', 40], ['Maria', 22]])
