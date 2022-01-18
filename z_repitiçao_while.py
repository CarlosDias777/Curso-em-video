c = 1 
while c < 10:
    print(c)
    c += 1
print('fim')

n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('fim')

r = 's'
while r == 's':
    a = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]')).lower()
print('fim')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um numero: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de numeros digitados foi de {}, são {} pares e são {} impares'.format(par+impar,par,impar))
