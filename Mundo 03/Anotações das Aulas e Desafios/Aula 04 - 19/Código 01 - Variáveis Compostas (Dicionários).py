"""
Tuplas: () - Parênteses
Listas: [] - Colchetes
Dicionários: {} - Chaves

Exemplo 1 de Dicionário Vazio:
dados = dict()

Exemplo 2 de Dicionário Vazio:
dados = {}

Exemplo de Dicionário Preenchido com 1 Linha:
dados = {'nome': 'Pedro', 'idade': 25}

Exemplo de Dicionário Preenchido com Múltiplas Linhas:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
"""
dados = {'nome': 'Pedro', 'idade': 25}  # Cria uma dicionário "dados" com os índices 'nome' (Pedro) e 'idade' (25)
print(dados['nome'])  # Exibe Pedro
print(dados['idade'])  # Exibe 25

dados['sexo'] = 'M'  # Adiciona o índice 'sexo' com o valor 'M' ao final do dicionário "dados"
del dados['idade']  # Deleta o índice 'idade' (com o valor 25) do dicionário "dados"
