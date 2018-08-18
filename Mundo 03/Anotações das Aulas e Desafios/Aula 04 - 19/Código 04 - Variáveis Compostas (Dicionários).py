pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}  # Cria um dicionário "pessoas" com 3 chaves e 3 valores
print(pessoas)  # Exibe {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])  # Exibe Gustavo
print(pessoas['idade'])  # Exibe 22

"""  NOTA: Usar aspas duplas no índice do dicionário em prints formatados, para não dar erro. """
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')  # Exibe O Gustavo tem 22 anos.

print(pessoas.keys())  # Exibe dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())  # Exibe dict_values(['Gustavo', 'M', 22])
print(pessoas.items())  # Exibe dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

for k in pessoas.keys():  # Para cada chave "k" nas chaves (keys) do dicionário "pessoas"...
    print(k)  # Exibe a chave "k" atual

for v in pessoas.values():  # Para cada valor "v" nos valores (values) do dicionário "pessoas"...
    print(v)  # Exibe a o valor "v" atual

for k, v in pessoas.items():  # Para cada chave "k" e valor "v" nos itens do dicionário "pessoas"...
    print(f'{k} = {v}')  # Exibe formatado a chave "k" e o valor "v" atuais

del pessoas['sexo']  # Deleta a chave 'sexo' (com o valor 'M') do dicionário "pessoas"
pessoas['nome'] = 'Leandro'  # Substitui o valor 'Gustavo' da chave 'nome' por 'Leandro', do dicionário "pessoas"
pessoas['peso'] = 98.5  # Adiciona a chave 'peso' com o valor 98.5 ao final do dicionário "pessoas"

print(pessoas)  # Exibe o dicionário "pessoas" já modificado: {'nome': 'Leandro', 'idade': 22, 'peso': 98.5}
