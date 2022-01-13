print('\033[30;41m teste1\033[m')
print('\033[4;33;44m teste2\033[m')
print('\033[1;35;43m teste3\033[m')
print('\033[30;42m teste4\033[m')
print('\033[m teste5\033[m')
print('\033[35;47m teste6\033[m')

cores = {
'limpa':'\033[m',
'azul':'\033[34m',
'roxo':'\033[35m'}
print('Ola muito prazer em te {}conhecer{}!!!'.format(cores['roxo'],cores['limpa']))