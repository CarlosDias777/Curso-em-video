def lin():
    print('=-='*30)
def soma(a,b):
    s = a + b
    print(f'"A" vale {a}, e "B" vale {b} a soma entre eles resulta em {s}')

lin()
soma(a=4,b=5)
lin()
soma(b=10,a=25)


def contador(* num):
    for v in num:
        print(v, end=' ')
    print('\nFim')

lin()
contador(2,5,8,3)
lin()
contador(0,1,2,3)
lin()

def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2,4,7,10]
dobrar(valores)
print(valores)
