n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if n1 == n2:
    print('O numero {} é igual a {}'.format(n1,n2))
elif n1 > n2:
    print('O numero {} é maior que {}'.format(n1,n2))
else:
    print('O numero {} é maior que {}'.format(n2,n1))