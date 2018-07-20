"""
É possível começar uma lista vazia "valores" assim:

valores = []

Ou assim:

valores = list()
"""
valores = []  # Cria uma lista vazia "valores"
valores.append(5)  # Adiciona o número inteiro 5 à lista
valores.append(9)  # Adiciona o número inteiro 9 à lista
valores.append(4)  # Adiciona o número inteiro 4 à lista

for v in valores:  # Para cada item "v" na lista "valores"...
    print(f'{v}...', end=' ')  # Exibe o item atual

print('\n')  # Cria um espaçamento para melhor visualização

for c, v in enumerate(valores):  # Para cada índice "c" e item "v" na lista "valores"...
    print(f'Na posição {c} encontrei o valor {v}!')  # Exibe o índice e o item atuais
print('Cheguei ao final da lista.')  # Exibe uma mensagem após a execução do laço "for"
