pessoas = {'nome':'Carlos','idade':19,'sexo':'M','deletar':'del'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')

print('=-='*20)
del pessoas['deletar']
pessoas['nome'] = 'Gustavo'
pessoas['peso'] = 65.5

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('=-='*20)
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('=-='*20)
brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['uf'])

print('=-='*20)
estado = {}
Brasil = []
for a in range(0,3):
    estado['uf'] = str(input('Digite o nome de um estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    Brasil.append(estado.copy())
for a in Brasil:
    for b in a.values():
        print(b, end=' ')
        print()