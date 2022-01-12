a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite outro numero: '))
if a > b and a > c:
    print('{} foi o maior numero digitado!'.format(a))
elif b > a and b > c:
    print('{} foi o maior numero digitado!'.format(b))
else:
    print('{} foi o maior numero digitado!'.format(c))