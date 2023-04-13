dicionario = {'horse':'cheval', 'cat': 'chat', 'dog': 'chien'}
palavra = ['cat', 'lion', 'horse']

for i in palavra:
    if i in dicionario:
        print(f'{i} -> {dicionario[i]}')
    else:
        print(i, 'não esta no dicionario')