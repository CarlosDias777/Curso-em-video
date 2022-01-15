print('Numero pares entre 1 e o numero que vc escolher!')
num = int(input('Até qual numero quer a contagem? '))
print('Os numeros pares são:')
for a in range(1,num+1):
    if a % 2 == 0:
        print(a)

#forma inteligente
# for a in range(2,num+1,2):
#    print(a)
#         