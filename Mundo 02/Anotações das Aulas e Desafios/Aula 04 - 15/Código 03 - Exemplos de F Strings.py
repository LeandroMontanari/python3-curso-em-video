nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}.')  # Salário com 2 casas decimais
print(f'O {nome:^20} tem {idade} anos.')  # Nome centralizado e ocupando 20 caracteres
print(f'{nome:-^20}')  # Nome centralizado e ocupando 20 caracteres com "-" no lugar dos espaços
print(f'{nome:->20}')  # Nome alinhado à direita e ocupando 20 caracteres com "-" no lugar dos espaços
print(f'{nome:-<20}')  # Nome alinhado à esquerda e ocupando 20 caracteres com "-" no lugar dos espaços
