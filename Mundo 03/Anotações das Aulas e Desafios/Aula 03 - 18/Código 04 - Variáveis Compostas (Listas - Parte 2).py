galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]  # Cria uma lista composta "galera" com 4 listas
print(galera)  # Exibe [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])  # Exibe ['João', 19]
print(galera[0][0])  # Exibe João
print(galera[2][1])  # Exibe 13

for pessoa in galera:  # Para cada "pessoa" na lista composta "galera"...
    print(pessoa)  # Exibe todos os dados (nome e idade) da "pessoa" atual

for pessoa in galera:  # Para cada "pessoa" na lista composta "galera"...
    print(pessoa[0])  # Exibe apenas o índice[0] (nome) da "pessoa" atual

for pessoa in galera:  # Para cada "pessoa" na lista composta "galera"...
    print(pessoa[1])  # Exibe apenas o índice[1] (idade) da "pessoa" atual

for pessoa in galera:  # Para cada "pessoa" na lista composta "galera"...
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')  # Exibe todos os dados da "pessoa" atual formatados
