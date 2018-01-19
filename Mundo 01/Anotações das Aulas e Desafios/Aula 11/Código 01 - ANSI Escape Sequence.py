"""
Sempre que for necessário representar uma cor no terminal, a seguinte sequência deverá ser usada:
\033[<ESTILO_DO_TEXTO>;<COR_DO_TEXTO>;<COR_DO_FUNDO>m

Exemplo:
\033[0;33;44m

Voltar ao Padrão do Terminal:
\033[m

Fundo Branco com Texto Preto:
\033[7:30m

Lista de Estilos do Texto:
0 = None (Sem Estilo)
1 = Bold (Em Negrito)
4 = Underline (Sublinhado)
7 = Negative (Cores Invertidas)

Lista de Cores do Texto:
30 = Branco
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Roxo
36 = Azul Claro
37 = Cinza

Lista de Cores do Fundo:
40 = Branco
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Roxo
46 = Azul Claro
47 = Cinza
"""
print('\033[31mTexto vermelho')
print('\033[31;43mTexto vermelho e fundo amarelo')
print('\033[1;31;43mTexto vermelho em negrito e fundo amarelo')
print('\033[1;31;43mTexto vermelho em negrito e fundo amarelo apenas até o final do texto\033[m')
print('\033[4;30;45mTexto branco sublinhado e fundo roxo apenas até o final do texto\033[m')
print('\033[7;30mTexto preto e fundo branco apenas até o final do texto\033[m')
print('\033[1;7;30mTexto preto em negrito e fundo branco apenas até o final do texto\033[m')

a = 3
b = 5
print('Os valores são \033[1;31m{} em vermelho e negrito\033[m e \033[1;33m{} em amarelo e negrito\033[m'.format(a, b))

nome = 'Guanabara'
print('Olá, {}{}{}!'.format('\033[1;31m', nome, '\033[m'))  # Variável "nome" em vermelho e negrito

cores = {
    'limpa': '\033[m',
    'azul': '033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}

print('Olá, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))  # Variável "nome" em amarelo
