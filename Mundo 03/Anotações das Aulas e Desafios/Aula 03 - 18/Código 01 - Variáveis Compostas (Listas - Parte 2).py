"""
Exemplo de Lista Composta:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

Índices:

[0][0] = 'Pedro'
[0][1] = 25
[1][0] = 'Maria'
[1][1] = 19
[2][0] = 'João'
[2][1] = 32
"""
pessoal = list()  # Cria uma nova lista vazia "pessoal"
dados = ['Pedro', 25]  # Cria uma lista "dados" com uma string e um número inteiro
pessoal.append(dados[:])  # Adiciona todos os itens de "dados" a "pessoal", criando uma lista dentro da outra (composta)
print(pessoal)  # Exibe [['Pedro', 25]]

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]  # Cria uma lista composta "pessoas" com 3 listas dentro
print(pessoas[0][0])  # Exibe Pedro
print(pessoas[1][1])  # Exibe 19
print(pessoas[2][0])  # Exibe João
print(pessoas[1])  # Exibe ['Maria', 19]
