sal = float(input('Digite seu salario: '))
if sal > 1250:
    print('O aumento do seu salario foi de 10% resultando em {} R$'.format(sal+(sal*0.1)))
else:
    print('O aumento do seu salario foi de 15% resultando em {} R$'.format(sal+(sal*0.15)))