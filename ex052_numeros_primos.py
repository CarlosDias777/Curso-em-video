#Gambiara mas funcionou k
num = int(input('Digite um numero: ')) 
s = 1
b = ''
string = ''
for a in range(1,num):
    s += 1   
    if num % s == 1:
        e_primo = True
    elif num % s == 0:
        e_primo = False
    string = str(e_primo)
    b += string
e_ou_n_primo = 'False' in b
if e_ou_n_primo == False:
    print('O numero é primo!')
else:
    print('O numero não é primo')




#forma q o guanarabara fez
"""
num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m',end=' ')
        tot += 1
    else:
        print('\033[31m',end=' ')
    print(c,end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
"""
    
