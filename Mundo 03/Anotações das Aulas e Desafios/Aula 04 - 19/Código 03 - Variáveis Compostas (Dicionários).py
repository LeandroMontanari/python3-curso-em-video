filme1 = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'}  # Cria um dicionário "filme1" com 3 chaves (keys) e 3 valores (values)

filme2 = {'titulo': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'}  # Cria um dicionário "filme2" com 3 chaves (keys) e 3 valores (values)

filme3 = {'titulo': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachowski'}  # Cria um dicionário "filme3" com 3 chaves (keys) e 3 valores (values)

locadora = list()  # Cria uma nova lista vazia "locadora"

locadora.append(filme1)  # Adiciona o dicionário "filme1" inteiro ao final da lista "locadora", como índice [0]
locadora.append(filme2)  # Adiciona o dicionário "filme2" inteiro ao final da lista "locadora", como índice [1]
locadora.append(filme3)  # Adiciona o dicionário "filme3" inteiro ao final da lista "locadora", como índice [2]

print(locadora[0]['ano'])  # Exibe o valor da chave "ano" contida no índice [0] ("filme1") de "locadora": 1977
print(locadora[2]['titulo'])  # Exibe o valor da chave "titulo" contida no índice [2] ("filme3") de "locadora": Matrix
