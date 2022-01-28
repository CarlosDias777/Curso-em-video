def leiaint():
    while True:
        n = input('Digite um numero: ')
        if n.isnumeric():
            print(f'Voce acabou de digitar o numero {n}')
            break
        else:
            print('\033[1;31mErrO! Digite um numero inteiro valido.\033[m')


leiaint()