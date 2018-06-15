"""
Exemplo de Lista (Variável Composta):
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
Índices:      [0]        [1]      [2]      [3]

NOTA 1: As Listas são MUTÁVEIS, ou seja, podem ser modificadas (diferente das Tuplas)!

NOTA 2: Listas são identificadas por "[]" (colchetes).
"""
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']  # Cria uma lista "lanche" com 4 itens (índices [0] a [3])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

lanche[3] = 'Picolé'  # Substitui o índice [3] ('Pudim') da lista "lanche" por 'Picolé'
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Picolé'], com a lista já modificada pelo comando anterior

lanche.append('Cookie')  # Adiciona o item 'Cookie' ao final da lista "lanche", deixando-o na posição 5 (ou índice [4])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Pizza', 'Picolé', 'Cookie'], com a lista novamente modificada
# Índices:                  [0]         [1]     [2]      [3]        [4]

""" NOTA: O índice [0] anterior ('Hambúrguer') não é substituído, apenas realocado para [1]. """
lanche.insert(0, 'Cachorro Quente')  # Insere o item 'Cachorro Quente' no índice [0] da lista "lanche"
print(lanche)  # Exibe ['Cachorro Quente', 'Hambúrguer', 'Suco', 'Pizza', 'Picolé', 'Cookie']
# Índices:                     [0]             [1]         [2]     [3]      [4]        [5]

""" NOTA: Assim como no comando anterior, todos os índices a partir daquele modificado ([3]) são realocados. """
del lanche[3]  # Deleta o índice [3] ('Pizza') da lista "lanche"
print(lanche)  # Exibe ['Cachorro Quente', 'Hambúrguer', 'Suco', 'Picolé', 'Cookie']
# Índices:                     [0]             [1]         [2]     [3]        [4]

""" NOTA: Os índices também são realocados após usar este método, como acontece com todos que modificam a lista. """
lanche.pop(0)  # Similar ao comando "del" anterior, deleta o índice [0] ('Cachorro Quente') da lista "lanche"
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Picolé', 'Cookie']
# Índices:                  [0]         [1]     [2]        [3]

lanche.pop()  # Usado sem especificar um valor entre parênteses, o método "pop()" deleta o último índice da lista ([3])
print(lanche)  # Exibe ['Hambúrguer', 'Suco', 'Picolé']
# Índices:                  [0]         [1]     [2]

""" NOTA: Se a lista possuir mais de um item igual ao especificado, apenas o primeiro existente é removido. """
lanche.remove('Suco')  # Ao invés do índice, no método "remove()", deleta-se o item especificado entre parênteses
print(lanche)  # Exibe ['Hambúrguer', 'Picolé']
# Índices:                  [0]         [1]

"""
A lista "lanche" atual contém apenas os itens 'Hambúrguer' e 'Picolé' (índices [0] e [1], respectivamente).
Ao tentar remover um item que não se encontra na lista, o Python retornará uma mensagem de erro. Por exemplo:

lanche.remove('Pastel')

Para solucionar este possível erro, partindo do pressuposto que o programador não sabe se
determinado item se encontra de fato na lista, pode-se utilizar, por exemplo, o comando:

if 'Pastel' in lanche:
    lanche.remove('Pastel')
"""

if 'Pastel' in lanche:  # Se o item 'Pastel' estiver presente na lista "lanche"...
    lanche.remove('Pastel')  # Remove o item 'Pastel' da lista "lanche"
else:  # Senão...
    print("A lista não possui o item 'Pastel'.")  # Exibe uma mensagem
