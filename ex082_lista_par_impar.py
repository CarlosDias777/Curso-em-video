lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar?[S/N] '))
    while continuar not in 'sn':
         continuar = str(input('Quer continuar?[S/N] '))
    if continuar == 'n':
        break
for a in range(0,len(lista)):
    if lista[a] % 2 ==0:
        par += lista[a],
    else:
        impar += lista[a],
print('=-='*20)
print(f"""A lista digitada completa é {lista}
A lista digitada so com os numeros pares é {par}
A lista digitado so com os numeros impares é {impar}""")