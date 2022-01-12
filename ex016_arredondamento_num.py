from math import ceil, floor, trunc
n = float(input('Digite algum valor: '))
print('O valor {} aredondado para baixo é de {} \nE arredondado para cima é de {}, sua porção inteira é {}'
.format(n,floor(n),ceil(n),trunc(n)))