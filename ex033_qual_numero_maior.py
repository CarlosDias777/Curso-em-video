#Modo que eu fiz
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite outro numero: '))
if a > b and a > c:
    print('{} foi o maior numero digitado!'.format(a))
elif b > a and b > c:
    print('{} foi o maior numero digitado!'.format(b))
else:
    print('{} foi o maior numero digitado!'.format(c))
if a < b and a < c:
    print('{} foi o menor numero digitado!'.format(a))
elif b < a and b < c:
    print('{} foi o menor numero digitado!'.format(b))
else:
    print('{} foi o menor numero digitado!'.format(c))

#forma que o guanabara fez
"""a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))"""