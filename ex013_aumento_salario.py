salario = float(input('Digite seu salario: '))
aumento = float(input('Digite o aumento do seu salario em %: '))
total = salario + ((salario * aumento) / 100)
print('O salario de {} com o aumento de {}% resulta em {}'.format(salario,aumento,total))