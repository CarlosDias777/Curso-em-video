valor = int(input('Digite um valor para P.A: '))
razao = int(input('Digite uma razão para P.A: '))
contador = int(input('Quantos termos? ')) + 1
contadortermos = contador
while contador != 0:
    contador -= 1
    if contador != 0:
        resul = print('{}'.format(valor),end=' → ')
    elif contador == 0:
        resul = print('{}'.format(valor),end=' ')
    if contador == 1:
        contador = int(input('\nSe quiser parar digite 0, senão digite quantos termos quer a mais: ')) + 1
        contadortermos += contador
    valor += razao
print('=!=!= FIM =!=!=')
print('{} termos mostrados'.format(contadortermos))