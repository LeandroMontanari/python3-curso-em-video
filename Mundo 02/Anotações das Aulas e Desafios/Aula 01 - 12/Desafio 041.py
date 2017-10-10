from datetime import date
atual = date.today().year
nas = int(input('Em que ano o atleta nasceu (ex: 1990)? '))
ani = str(input('Este ano o atleta já fez aniversário? Digite S para sim ou N para não: ')).upper().strip()
if ani == 'S' or ani == 'SIM':
    idade = atual - nas
elif ani == 'N' or ani == 'NAO' or ani == 'NÃO':
    idade = atual - nas - 1
else:
    print('Você digitou uma resposta inválida!')
if idade <= 9:
    print('O atleta de {} anos vai ficar na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('O atleta de {} anos vai ficar na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('O atleta de {} anos vai ficar na categoria JUNIOR!'.format(idade))
elif idade <= 25:
    print('O atleta de {} anos vai ficar na categoria SÊNIOR!'.format(idade))
elif idade > 25:
    print('O atleta de {} anos vai ficar na categoria MASTER!'.format(idade))
