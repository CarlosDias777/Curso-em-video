frase = '   Curso em Video Python   '
f2 = frase.strip() # tira os espaços antes e dps do frase
print(f2) 
print(frase[3])
print(frase[:5])
print(frase[5:])
print(frase[0::2])
print(len(frase)) #Contar quantidade de caracteres
print(frase.count('o')) #contar caractere especifico
print(frase.replace('Video', 'jornal'))
print('Python' in frase)
print(frase.find('em'))
print(frase.find('android'))
print(frase.strip().replace('Curso','Urso'))
print(frase.split())

print('-'*25)

print("""Assim que faz um print
em mais de uma linha, finalmente aprendi """)