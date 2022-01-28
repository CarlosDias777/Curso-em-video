from time import sleep
def contagem(a,b,c):
    #if c == 0:   c = 1 forma mais eficiente de mudar o contador de 0 para 1
    
    c = abs(c)
    if a < b:
        if c == 0:
            for r in range(a,b+1,1):
                print(r,end=' ',flush=True)
                sleep(0.25)
            print('\nFim')
        else:
            for r in range(a,b+1,c):
                print(r,end=' ',flush=True)
                sleep(0.25)
            print('\nFim')
    elif a > b:
        if c == 0:
            for r in range(a,b+1,-1):
                print(r,end=' ',flush=True)
                sleep(0.25)
            print('\nFim')
        else:
            for r in range(a,b-1,-c):
                print(r,end=' ',flush=True)
                sleep(0.25)
            print('\nFim')


print('Contagem de 0 ate 10 de 1 em 1:')
contagem(0,10,1)
print('Contagem de 10 ate 0 de 2 em 2')
contagem(10,0,2)

inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
if passo == 0:
    print(f'contagem de {inicio} ate {final} de 1 em 1')
else:
    print(f'contagem de {inicio} ate {final} de {passo} em {passo}')
contagem(inicio,final,passo)