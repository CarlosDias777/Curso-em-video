for a in range(0,5):
    print('oi')
print('=!='*15)

for b in range(0,5):
    print(b)
print('=!='*15)

for c in range(6,0,-1):
    print(c)
print('=!='*15)

for d in range(0,10,3):
    print(d)
print('=!='*15)

num = int(input('Digite um numero: '))
for e in range(0, num+1):
    print(e)
print('=!='*15)

s = 0 
for f in range(0,3):
    n = int(input('Digite um numero: '))
    s += n
print('A soma dos numeros foi de {}'.format(s))
