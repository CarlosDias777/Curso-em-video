valor1 = int(input('Digite quanto quer sacar do caixa eletronico?R$ '))
valor = valor1
cont = 0
ced = 50
while True:
    if valor >= ced:
        valor -= ced
        cont += 1
    else:
        cont = 0

        if cont > 0:
            print(f'Total de {cont} cedulas de {ced}')
        
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        
        if valor == 0:
            break

