valores = list()  # Cria uma lista vazia "valores"
for cont in range(0, 5):  # Para cada número "cont" de 0 até 4 (lembrando que o 5 é ignorado)...
    valores.append(int(input('Digite um valor: ')))  # Adiciona o número digitado pelo usuário à lista "valores"

for c, v in enumerate(valores):  # Para cada índice "c" e item "v" na lista "valores"...
    print(f'Na posição {c} encontrei o valor {v}!')  # Exibe o índice e o item atuais
print('Cheguei ao final da lista.')  # Exibe uma mensagem após a execução do laço "for"
