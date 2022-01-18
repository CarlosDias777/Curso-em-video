valor = int(input('Digite um valor para P.A: '))
razao = int(input('Digite uma razão para P.A: '))
contador = 10
while contador != 0:
    contador -= 1
    if contador != 0:
        resul = print('{}'.format(valor),end=' → ')
    elif contador == 0:
        resul = print('{}'.format(valor),end=' ')
    valor += razao
