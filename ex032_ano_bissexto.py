ano = int(input('Digite algum ano: '))
negativo = ano < 0
if negativo == True:
    print('Ano invalido!')
elif ano % 4 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))