frase = input('Digite uma frase: ').upper().strip()
qtd = frase.count('A')
pos1 = frase.find('A')+1
pos2 = frase.rfind('A')+1
print('\nA sua frase tem {} letra(s) "A". A primeira aparece na posição número {} e a última aparece na posição número {}!'.format(qtd, pos1, pos2))