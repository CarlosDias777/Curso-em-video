from ast import JoinedStr


a = s = 0
while True:
    print(a)
    a += 1
    if a == 1000:
        break
    s += a
print(f'A soma de 0 ate 1000 resulta em {s}')

b = c = 0
while True:
    b = int(input('Digite um numero: '))
    if b == 999:
        break
    c += b
print(f'A soma dos valores digitados vezes 2 resulta em {c*2:.2f}')

nome = 'Jose'
print(f'{nome:=^20}')
# centraliza = ^, alinha a direira = >, alinhar a esqueda = <