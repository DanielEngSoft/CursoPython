import time


def Contador(i, f, p):
    if p == 0:
        p = 1
    if i > f:
        f -= 1
        if p >= 0:
            p *= -1
    else:
        f += 1
        if p < 0:
            p *= -1
    print('-='*20)

    for c in range(i, f, p):
        print(c, end=' ')
        time.sleep(0.3)
    print('FIM!')


Contador(1, 11, 1)
Contador(10, -1, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
Contador(i, f, p)
'''Daniel'''
