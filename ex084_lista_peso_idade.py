lista = []
dado = []
menor = maior = 0
while True:
    dado.append(str(input('Nome da pessoa: ')))
    dado.append(float(input('Peso da pessoa: ')))
    
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]


    lista.append(dado[:])
    dado.clear()
    
    conti = str(input('Quer continuar?[s/n] ')).lower()

    while conti not in 'sn':
        conti = str(input('Quer continuar?[s/n] ')).lower()


    if conti == 'n':
        break
print(lista)    

print(f'{len(lista)} foi a quantidade de pessoas cadastradas')
print('As pessoas com maiores pesos são ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}! ',end='')
print('\nAs pessoas com menores pesos são ',end='')
for p in lista:        
    if p[1] == menor:
        print(f'{p[0]}! ',end='')