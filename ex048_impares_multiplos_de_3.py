print('A soma dos numeros impares e que são multiplos de 3 entre 1 e 500 é')
var = 0
for a in range(1,501,2):
    if a % 3 == 0:
        var = var + a
print(var)
