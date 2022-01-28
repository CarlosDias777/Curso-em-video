def texto(txt):
    c = len(txt) + 4
    print('~'*c)
    print(f'  {txt}')
    print('~'*c)

t = str(input('Digite uma frase: '))
texto(t)