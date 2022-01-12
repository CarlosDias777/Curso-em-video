nome = str(input('Digite seu nome: ')).strip()
res  = nome.lower().find('silva')
if res == 0:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')