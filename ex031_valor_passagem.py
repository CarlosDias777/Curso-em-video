km = float(input('Qual a distancia da sua viagem em KMS: '))
if km <= 200:
    print('O valor da sua passagem é de {} R$'.format(km*0.5))
else:
    print('O valor da sua passagem é de {} R$'.format(km*0.45))
