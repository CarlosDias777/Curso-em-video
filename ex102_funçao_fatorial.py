def fatorial(n=1,show=False):
    """Calcula o fatorial de um numero
    param n = O numero a ser calculado
    param show(opcional) = Mostra o calculo no console
    param return = none
    """
    f = 1
    if show == False:
        for a in range(n,0,-1):
            f *= a
            print(f)
    else:
        for a in range(n,0,-1):
            f *= a
            if a != 1:
                print(f'{a} X',end=' ')
            else:
                print(f'{a} ',end='')
        print(f'= {f}')

help(fatorial)
