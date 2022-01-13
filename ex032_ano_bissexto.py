from datetime import date
ano = int(input('Digite algum ano, se o ano digitado for 0 sera analisado o ano presente: '))
negativo = ano < 0
if ano == 0:
    ano = date.today().year
if negativo == True:
    print('Ano invalido!')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))