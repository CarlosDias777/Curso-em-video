frase = str(input('Digite uma frase: ')).strip().split()
#s = len(frase) - 1 
string = ''
frase_string = ''
tamanho_frase = len(frase)
contadormais = 0

#Tirar espaços da frase
for b in range(0,tamanho_frase):
    frase_string += frase[contadormais]
    contadormais += 1
"""Como o guanabara fez
frase = str(input('digite uma frase: ').strip().upper()
palavras = frase.split()
JUNTO = ''.join(palavras)"""

#Inverte a frase
contadormenos = len(frase_string) - 1
for a in range(0,contadormenos+1):
    string += frase_string[contadormenos]
    contadormenos -= 1
"""Como o guanabara fez
for frase in range(len(junto) -1,-1,-1)
    inverso += junto[letra]
OU
inverso = junto[::-1]"""

#Da o resultado
if frase_string.lower() == string.lower():
    print('A frase {}, invertida fica {}, portanto é um \033[1;32mPALINDROMO\033[m'.format(frase_string,string))
else:
    print('A frase {}, invertida fica {}, portanto não é um \033[1;31mPALINDROMO\033[m'.format(frase_string,string))
