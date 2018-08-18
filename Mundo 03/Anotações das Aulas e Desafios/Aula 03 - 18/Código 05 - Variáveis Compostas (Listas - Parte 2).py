galera = list()  # Cria uma nova lista vazia "galera"
dado = list()  # Cria uma nova lista vazia "dado"
totmai = totmen = 0  # Cria duas variáveis simples "totmai" e "totmen" com valor 0

for c in range(0, 3):  # Cria um laço "for" que será executado 3 vezes (números de 0 a 2)
    dado.append(str(input('Nome: ')))  # Adiciona a string digitada ao final da lista "dado"
    dado.append(int(input('Idade: ')))  # Adiciona o número inteiro digitado ao final da lista "dado"
    galera.append(dado[:])  # Adiciona uma cópia da lista "dado" atual ao final da lista composta "galera"
    """ NOTA: Lembrar sempre de usar "lista[:]" ao invés de "lista[]" para fazer uma cópia da lista em questão. """
    dado.clear()  # Esvazia a lista "dado"

print(galera)  # Exibe todos os itens digitados no laço "for" anterior, guardados na lista composta "galera"

for pessoa in galera:  # Para cada "pessoa" na lista composta "galera"...
    if pessoa[1] >= 21:  # Se o índice [1] (idade) atual for maior ou igual a 21...
        print(f'{pessoa[0]} é maior de idade.')  # Exibe que o índice [0] (nome) da "pessoa" atual é maior de idade
        totmai += 1  # Acrescenta 1 à variável simples "totmai"
    else:  # Senão...
        print(f'{pessoa[0]} é menor de idade.')  # Exibe que o índice [0] (nome) da "pessoa" atual é menor de idade
        totmen += 1  # Acrescente 1 à variável simples "totmen"

print(f'Temos {totmai} maiores e {totmen} menores de idade.')  # Exibe os números finais de "totmai" e "totmen"
