vel = float(input('Qual a velocidade do carro: '))
if vel > 80:
    print('Voce está sendo multado por ultrapassar o limite de velocidade!\nO valor a pagar da multa é de {} R$'
    .format((vel-80)*7))
else:
    print('Parabens, voce esta dentro do limite de velocidade, continue assim!')