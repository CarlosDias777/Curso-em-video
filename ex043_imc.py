altura = float(input('Qual a sua altura em metros? '))
massa = float(input('Qual a sua massa(peso) em kg? '))
imc = massa / (altura * altura) #altura vezes 2 é diferente de altura vezes altura, wtf???
if imc < 18.5:
    print('Voce é MAGRO de acordo com o indice de massa corporal')
elif imc > 18.5 and imc < 25:
    print('Voce é NORMAL de acordo com o indice de massa corporal')
elif imc > 25 and imc < 30:
    print('Voce esta em SOBREPESO de acordo com o indice de massa corporal')
elif imc > 30 and imc < 40:
    print('Voce é OBESO de acordo com o indice de massa corporal')
else:
    print('Voce tem OBESIDADE MÓRBIDA de acordo com o indice de massa corporal')