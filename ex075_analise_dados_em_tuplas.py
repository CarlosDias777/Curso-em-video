lista = ()
par = ()
for a in range(1,5):
    if a == 1:
        num = int(input('Digite um numero: '))
    else:
        num = int(input('Digite outro numero: '))
    lista += num,
    if num % 2 == 0:
        par += num,
    
print(f"""O numero 9 apareceu {lista.count(9)} vezes
Os numeros pares digitados são {par}""")
if 3 not in lista:
    print('Não há nenhum numero 3 digitado')
else:
    print(f'O numero 3 foi digitado a primeira vez na posiçã {lista.index(3)+1}')
