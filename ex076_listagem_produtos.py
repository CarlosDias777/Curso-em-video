lista = ('Lapis',1.75,
'Borracha',2.00,
'Caderno',15.90,
'Mochila',120.32)
print(f'{"Listagem de Preços":^40}')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end ='')
    elif pos % 2 == 1:
        print(f'R$ {lista[pos]:>3.2f}')
print('=!='*20)