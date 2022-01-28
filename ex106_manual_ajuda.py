def ajuda(msg):
    return help(msg)


while True:
    print('Digite fim para parar!')
    resp = str(input('Digite a função que quer analisar:' ))
    if resp.strip().lower() == 'fim':
        break
    else:
        ajuda(resp)
    