frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra (A) aparece {} vezes na sua frase!'.format(frase.lower().count('a')))
print('A primeira vez que a letra a aparece é na posição:',frase.find('a')+1)
print('A ultima vez que a letra a aparece é na posição:',frase.rfind('a'))
