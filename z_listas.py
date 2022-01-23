num = [2,4,6,8]
num[0] = 0
num.append(10)
num.sort(reverse=True)
num.insert(4, 2)
num.pop(0)
if 2 in num:
    num.remove(2)
print(num)
print(f'Essa lista em {len(num)} elementos')

for a in num:
    print(f'{a}', end=' → ',)

for c, v in enumerate(num):
    print(f'\nNa posição {c} encontrei o valor {v}!')

lista = [1,3,4,6]
for a,v in enumerate(lista):
    print(a, v)

z = ['a','b','c']
y = z[:]
y[0] = 3
print(z)
print(y)