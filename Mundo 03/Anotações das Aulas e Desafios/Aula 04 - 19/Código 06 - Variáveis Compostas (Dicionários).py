estado = dict()  # Cria um novo dicionário vazio "estado"
brasil = list()  # Cria uma nova lista vazia "brasil"

"""
MÉTODO 1: Errado. Desse jeito, apenas os últimos valores digitados serão adicionados à lista repetidamente.
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado)
print(brasil)

MÉTODO 2: Errado. Desse jeito, o Python apresentará o erro "TypeError: unhashable type: 'slice'".
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado[:])
print(brasil)

MÉTODO 3: Correto. Desse jeito, o Python adicionará uma cópia do dicionário "estado" atual ao final da lista "brasil".
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
"""

for c in range(0, 3):  # Para cada número "c" de 0 a 2...
    estado['uf'] = str(input('Unidade Federativa: '))  # Atribui à chave 'uf' do dicionário "estado" o valor digitado
    estado['sigla'] = str(input('Sigla do Estado: '))  # Atribui à chave 'sigla' do dicionário "estado" o valor digitado
    brasil.append(estado.copy())  # Adiciona uma cópia do atual dicionário "estado" ao final da lista "brasil"
print(brasil)  # Exibe a lista "brasil" já preenchida com os estados

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    print(e)  # Exibe o dicionário "e" atual

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    for k, v in e.items():  # Para cada chave "k" e valor "v" nos itens do dicionário "e"...
        print(f'O campo {k} tem valor {v}.')  # Exibe formatado a chave "k" e o valor "v" atuais

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    for v in e.values():  # Para cada valor "v" nos valores do dicionário "e"...
        print(v, end=' ')  # Exibe o valor "v" atual com um espaço no final, sem quebrar a linha
    print()  # Dá uma quebra de linha
