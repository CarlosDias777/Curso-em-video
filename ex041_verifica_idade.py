from datetime import date
ano_atu = date.today().year
ano = int(input('Digite o ano(yyyy) em que nasceu: '))
idade = ano_atu - ano
if idade > 20:
    print('Sua categoria na confederação nacional de natação é MASTER')
elif idade <= 20 and idade > 19:
    print('Sua categoria na confederação nacional de natação é SÊNIOR')
elif idade <= 19 and idade > 14:
    print('Sua categoria na confederação nacional de natação é JUNIOR')
elif idade <= 14 and idade > 9:
    print('Sua categoria na confederação nacional de natação é INFANTIL')
else:
    print('Sua categoria na confederação nacional de natação é MIRIM')