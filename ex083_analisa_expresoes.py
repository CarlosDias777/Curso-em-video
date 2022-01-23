"""valor = str(input('Digite uma expressão matematica: '))
cont1 = valor.count('(')
cont2 = valor.count(')')
if cont1 != cont2:
    print('A expressão está errada!')
else:
    print('A expressão esta correta')
"""

expr = str(input('Digite uma expressão: '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')

    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')