#Forma que fiz
"""print('Digite a idade de cada pessoa')
for a in range(1,8):
    idade = int(input('Qual a idade? '))
    print('=!='*15)
    if idade > 18:
        print('Voce é maior de idade')
    else:
        print('Voce não é maior de idade')
    print('=!='*15)"""

from datetime import date
atual = date.today().year
contagemmaior = 0
contagemmenor = 0
for a in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(a)))
    idade = atual - nasc
    if idade > 18:
        contagemmaior += 1
    else:
        contagemmenor += 1
print('Ao todo existem {} maiores de idade, e {} menores de idade'.format(contagemmaior,contagemmenor))