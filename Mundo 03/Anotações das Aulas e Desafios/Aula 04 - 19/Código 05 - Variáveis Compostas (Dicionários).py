brasil = list()  # Cria uma nova lista vazia "brasil"
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # Cria um dicionário "estado1" com 2 chaves e 2 valores
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  # Cria um dicionário "estado2" com 2 chaves e 2 valores
brasil.append(estado1)  # Adiciona o dicionário "estado1" inteiro ao final da lista "brasil", como índice [0]
brasil.append(estado2)  # Adiciona o dicionário "estado2" inteiro ao final da lista "brasil", como índice [1]

print(estado1)  # Exibe {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2)  # Exibe {'uf': 'São Paulo', 'sigla': 'SP'}

print(brasil)  # Exibe [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0])  # Exibe {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1])  # Exibe {'uf': 'São Paulo', 'sigla': 'SP'}

print(brasil[0]['uf'])  # Exibe Rio de Janeiro
print(brasil[1]['uf'])  # Exibe São Paulo

print(brasil[0]['sigla'])  # Exibe RJ
print(brasil[1]['sigla'])  # Exibe SP
