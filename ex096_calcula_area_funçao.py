def texto(txt):
    print('=-='*20)
    print(f'{txt:^60}')
    print('=-='*20)


texto("Controle de terreno")
lar = float(input('Digite a largura do terreno em metros: '))
comp = float(input('Digite o comprimento do terreno em metros: '))


def area(a,b):
    r = lar * comp
    print(f'A largura do terreno mede {a} o comprimento mede {b} e a area do terreno mede {r}m²')


area(lar,comp)