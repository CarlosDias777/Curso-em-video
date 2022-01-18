n1 = int(input('Digite um valor para sequencia de fibonacci: '))
primeiro_n = n1
termo = int(input('Digite quantos termos para a sequencia: '))
contagem_termo = termo
total = 0
total2 = 0
while contagem_termo != 0:
    if contagem_termo == termo:
        total = n1 + 1
        print('{} + {} = {}'.format(n1,'1',total))
    elif contagem_termo == termo -1:
        total2 = total + n1
        print('{} + {} = {}'.format(total,n1,total2))
        n1 = total
        total = total2
    else:
        total2 = total + n1
        print('{} + {} = {}'.format(total,n1,total2))
        n1 = total
        total = total2
    contagem_termo -= 1
print('A sequencia de fibonacci de {}, com {} termos, resulta em {}!!'.format(primeiro_n,termo,total2))
