"""
DESAFIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""
nome = input('Digite seu nome completo: ')
nome_sem_espacos = len(nome) - nome.count(' ')
primeiro_nome = len(nome.split()[0])
print('\nNome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('Quantidade total de letras (sem contar os espaços): {}'.format(nome_sem_espacos))
print('Quantidade de letras do primeiro nome: {}'.format(primeiro_nome))
