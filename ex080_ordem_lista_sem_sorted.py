#como eu fiz
"""lista = []
maior = menor = 0
for a in range(0,5):
    valor = int(input('Digite um valor: '))
    if a == 0:
        lista.append(valor)
        menor = maior = valor
        print('Adicionando no final da lista')
    else:
        
        if valor > maior:
            lista.insert(lista.index(maior)+1,valor)
            print('Adicionando no final da lista')
        elif valor < menor:
            lista.insert(lista.index(menor),valor)
            print('Adicionando no inicio da lista')
        elif valor < maior:
            lista.insert(lista.index(maior),valor)
            print(f'Adicionando na posiçao {lista.index(maior)}')
        elif valor > menor:
            lista.insert(lista.index(menor),valor)
            print(f'Adicionando na posição {lista.index(menor)}')
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
            
print(f'Os valores em ordem: {lista}')"""

lista = []
for a in range(0,5):
    n = int(input('Digite um valor: '))
    if a == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionando a ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos}')
                break
            pos += 1  
print('=!='*20)
print(f'Os valores digitados em ordem foram {lista}')  