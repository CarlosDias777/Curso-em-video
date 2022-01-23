lista = ('Aprender','Programar','Linguagem','Python')
for a in lista:
    print(f'\nNa palavra {a} temos as vogais ', end='')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
