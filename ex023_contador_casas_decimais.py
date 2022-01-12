n = input('Digite um numero de 0 ate 9999: ')
u = int(n) // 1 % 10
d = int(n) // 10 % 10
c = int(n) // 100 % 10
m = int(n) // 1000 % 10
if len(n) > 4 or int(n) < 0:
    print('Numero invalido!')
else:
    print('''O numero escolhido foi {}
Sua unidade vale: {}
Sua dezena vale: {}
Sua centena vale: {}
Seu milhar vale: {}'''.format(n,u,d,c,m))



