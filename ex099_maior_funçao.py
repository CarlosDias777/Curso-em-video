def maior(*n):
    m = 0
    for k,v in enumerate(n):
        print(v, end=' ')
        if k == 0:
            m = v 
        else:
            if v > m:
                m = v

    print(f'\nForam analisados {len(n)} numeros e o maior numero é {m}  ')


maior(1,7,8,6)
maior(21,32,51,4,5)