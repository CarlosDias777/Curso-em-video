n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
oper = 0
print('=!='*20)
print("""Qual operação devo fazer com os valores digitados??
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR VALOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA""")
while oper != 5:
    print('=!='*20)
    oper = int(input('O que devo fazer? '))
    print('=!='*20)
    if oper == 1:
        print('A soma de {} e {} resulta em {}!'.format(n1,n2,n1+n2))
    elif oper == 2:
        print('A multiplicação de {} e {} resulta em {}!'.format(n1,n2,n1*n2))
    elif oper == 3:
        if n1 > n2:
            print('O maior valor digitado é {}!'.format(n1))
        elif n2 > n1:
            print('O maior valor digitado é {}!'.format(n2))
        else:
            print('Os valores {} e {} são iguais'.format(n1,n2))
    elif oper == 4:
        n1 = float(input('Digite outro valor: '))
        n2 = float(input('Digite outro valor: '))
    elif oper == 5:
        print('Finalizando programa!!')
    else:
        print('Operação invalida!! tente novamente')