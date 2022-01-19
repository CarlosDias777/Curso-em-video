while True:
    print('Se o numero for negativo o programa será interrompido!!')
    n = int(input('Digite um valor para ser calculado pela TABUADA3: ')) 
    print('=!='*20)
    if n < 0:
        break
    for a in range(1,11):
        print(f'{a} X {n} = {a*n}')
    print('=!='*20)
print('\033[1;35mFim dos calculos!!')
    