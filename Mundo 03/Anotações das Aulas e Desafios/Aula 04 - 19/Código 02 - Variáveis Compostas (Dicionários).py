filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}  # Cria um dicionário "filme" com 3 chaves (keys) e 3 valores (values)

print(filme.keys())  # Exibe as chaves do dicionário "filme"
print(filme.values())  # Exibe os valores do dicionário "filme"
print(filme.items())  # Exibe os itens (chave + valor) do dicionário "filme"

for k, v in filme.items():  # Para cada chave (k) e valor (v) nos itens do dicionário "filme"...
    print(f'O {k} é {v}')  # Exibe formatado a chave (k) atual e seu respectivo valor (v)
