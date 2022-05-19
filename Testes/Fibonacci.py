'''def fibonacci(x):
    cont = 0
    y = 0
    z = 1
    r = 0
    while cont < x:
        print(r)
        r = z
        z = y + z
        y = r
        cont = cont + 1
    return ''
x = int(input('Digite quantos números da sequencia de fibonacci deseja ver: '))
print(fibonacci(x))

''' '''
    0 1 1 2 3 5 8 r
    0 1 1 2 3 5 8 y
    1 2 3 5 8 13 z
    
    0 1 1 2 3 5 8
    '''
cont = 1
n = [0, 1]
num = int(input('Digite quantos numeros da sequencia deseja ver: '))
while cont < num-1:
    n.append(n[cont]+n[cont - 1])
    cont += 1
print(n)