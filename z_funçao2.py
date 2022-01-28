def teste():
    a = 5
    print(a)


a = 2
teste()
print(a)

print('-=-'*20)

def teste():
    global b
    b = 5
    print(a)


b = 2
teste()
print(a)

print('-=-'*20)

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

resp = somar(2,5,7)
print(resp)

print('-=-'*20)

def fatorial(n=1):
    f = 1
    for a in range(n,0,-1):
        f *= a
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f1,f2,f3)