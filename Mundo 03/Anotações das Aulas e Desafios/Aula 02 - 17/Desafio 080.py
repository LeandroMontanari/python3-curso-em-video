"""
DESAFIO 080: Lista Ordenada sem Repetições

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = list()
for n in range(1, 5 + 1):
    valor = int(input('Digite um valor: '))
    if n == 1 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(lista):
            if valor <= v:
                lista.insert(i, valor)
                print(f'Adicionado na posição {i} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
