contador = 0
pali = 0
f = str(input('Digite um frase: '))
ff = f.lower().strip().replace(' ', '')

ff = ff.replace('á', 'a')
ff = ff.replace('à', 'a')
ff = ff.replace('ã', 'a')
ff = ff.replace('â', 'a')
ff = ff.replace('é', 'e')
ff = ff.replace('ê', 'e')
ff = ff.replace('í', 'i')
ff = ff.replace('ó', 'o')
ff = ff.replace('ô', 'o')
ff = ff.replace('õ', 'o')
ff = ff.replace('ú', 'u')
ff = ff.replace('ç', 'c')
ff = ff.replace('"', '')
ff = ff.replace("'", "")
ff = ff.replace(',', '')
ff = ff.replace('.', '')
ff = ff.replace('!', '')
ff = ff.replace(';', '')
ff = ff.replace(':', '')
ff = ff.replace('?', '')
ff = ff.replace('-', '')
ff = ff.replace('_', '')

tff = len(ff)

for i in ff:
    contador += 1
    if i == ff[tff - contador:tff - contador + 1]:
        pali += 1
    else:
        pali = 0

if tff == pali:
    print('"{}" é um palíndromo.'.format(f))
else:
    print('"{}" não é um palíndromo.'.format(f))
