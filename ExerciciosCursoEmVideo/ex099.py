def Maior(*n):
    for c in range(0, len(n)):
        print(n[c], end=' ')
    print()
    print(f'O maior valor é {max(n)}')


Maior(5,6,4,12,5,3,2,0)