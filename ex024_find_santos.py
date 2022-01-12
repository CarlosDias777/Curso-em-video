cidade = str(input('Digite o nome da sua cidade: '))
lista = cidade.strip().lower().split()
if lista[0] == 'santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')