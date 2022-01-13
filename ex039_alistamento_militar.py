from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano(yyyy) que nasceu: '))
if ano_atual - ano_nasc == 18:
    print('Voce deve se apresentar para o alistamento militar obrigatorio!!!')
elif ano_atual - ano_nasc < 18:
    print('Voce ainda é menor de idade,não precisa de alistar, mas em {} anos sua apresentação é obrigatoria'
    .format(18 - (ano_atual - ano_nasc)))
else:
    print('Sua apresentação no alistamento militar ja passou faz {} anos'.format((ano_atual - ano_nasc) - 18))