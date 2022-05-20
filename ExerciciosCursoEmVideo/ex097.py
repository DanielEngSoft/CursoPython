def Escreva(frase):
    t = len(frase) + 4
    print('~' * t)
    print(' ', frase)
    print('~' * t)


c = str(input('Frase: '))
Escreva(c)
