num = int(input('Digite um numero a ser fatorado: '))
contador = num -1
conta = num
while contador != 0:
    if contador == num - 1:
        print('Fatorando {} por {} resultado em {}'.format(num,contador,num*contador))
    else:
        print('Fatorando {} por {} resultado em {}'.format(conta,contador,conta*contador))
    conta *= contador    
    contador -= 1
print('=!='*20)
print('O numero {} fatorado resulta em {}!'.format(num,conta))

#forma com modulos
"""from math import factorial
n = int(input('Digite um numero'))
f = factorial(n)"""