teste = []
teste.append('Carlos')
teste.append(19)
galera = []
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 25
galera.append(teste[:])
print(teste)
print(galera)

geral = [['Heitor',16], ['Gustavo', 40], ['Carlos',19], ['Maria', 28]]
for a in geral:
    print(f'A pessoa {a[0]} tem {a[1]} anos de idade ')