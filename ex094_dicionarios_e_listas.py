lista = []
while True:
    nsi = {}

    nsi['nome'] = str(input('Digite o nome da pessoa: '))

    nsi['sexo'] = str(input('Digite o sexo da pessoa:[M/F] ')).upper()
    while nsi['sexo'] not in 'MF':
        nsi['sexo'] = str(input('Digite o sexo da pessoa:[M/F] ')).upper()

    nsi['idade'] = int(input('Digite a idade da pessoa: '))

    lista.append(nsi.copy())
    
    nsi.clear()
    
    continuar = str(input('Quer continuar?[S/N] ')).lower()
    while continuar not in 'sn':
        continuar = str(input('Quer continuar?[S/N] ')).lower()
    if continuar == 'n':
        break

print(f'Foram cadastradas um total de {len(lista)} pessoas')

mulheres = []
media = 0
for a in lista:
    media += a['idade']
    if a['sexo'] == 'F':
        mulheres.append(a['nome'])
media /= len(lista)

acimamedia = []
for i in lista:
    if i['idade'] > media:
        acimamedia.append(i['nome'])

print(f'A media de idade das pessoas cadastradas é de {media}')
print(f'Lista de todas as mulheres que foram cadastradas digitadas {mulheres}')
print(f'Lista com todas as pessoas com idade acima da media {acimamedia}')
