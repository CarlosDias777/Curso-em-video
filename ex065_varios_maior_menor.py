continuar = ''
acumulador = 0
contador = 0
maior = ''
menor = ''
valor = 0
while continuar != 'n':
    valor = int(input('Digite o valor: '))
    continuar = str(input('Quer continuar digitando valores?[S/N] ')).lower().strip()
    acumulador += valor
    contador += 1
    if contador == 1:
        menor = maior = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
print('A media dos valores digitados foi de {} e foram {} numeros digitados'.format(acumulador/contador,contador))
    