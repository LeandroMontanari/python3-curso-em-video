"""
NOTA 1: Todo método tem "()" (abre e fecha parênteses) no final.
Por exemplo, em "carro.siga()", "carro" é o objeto e "siga()" é o método.

NOTA 2: Todos os exercícios e desafios feitos até o momento utilizaram Estruturas Sequenciais.
A partir de agora, serão apresentadas as Estruturas Condicionais.

NOTA 3: O espaçamento lateral antes dos comandos dentro de uma Estrutura Condicional é chamado Indentação.
Uma indentação pode ser criada pressionando a tecla "Tab" (2 teclas abaixo do "Esc").

NOTA 4: Em uma Estrutura Condicional simples de "se" e "senão", o bloco de comando do "se" é
executado se a condição for verdadeira (True), enquanto o bloco de comandos do "senão" é
executado se a condição for falsa (False).

Exemplo de Condicional Simples:
if <CONDIÇÃO>:
    <COMANDOS>

Exemplo de Condicional Composta:
if <CONDIÇÃO>:
    <COMANDOS A>
else:
    <COMANDOS B>

Exemplo de Condicional Simplificada:
print('Frase a exibir se a condição se cumprir' if <CONDIÇÃO> else 'Frase a exibir se a condição não se cumprir')
"""
tempo = int(input('Quantos anos tem seu carro? '))  # Atribui à variável "tempo" o valor de um número inteiro
if tempo <= 3:  # Se a variável "tempo" receber um valor igual ou menor do que 3...
    print('Carro novo!')  # Exibe "Carro novo!"
else:  # Senão...
    print('Carro velho!')  # Exibe "Carro velho!"
print('--- FIM ---')  # Exibe "--- FIM ---" independemente do resultado da condição acima
