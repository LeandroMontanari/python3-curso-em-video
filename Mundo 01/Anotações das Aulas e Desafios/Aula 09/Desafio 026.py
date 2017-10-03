frase = input('Digite uma frase: ').upper().strip()
qtd = frase.count('A')
pos1 = frase.find('A')+1
pos2 = frase.rfind('A')+1
print('\nA sua frase tem {} letra(s) "A".'.format(qtd), end='\n')
print('A primeira aparece na posição número {}\ne a última aparece na posição número {}!'.format(pos1, pos2))
