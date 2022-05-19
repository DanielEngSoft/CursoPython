x = 0
mn = 0
cont = [None] * 10
while x < 10:
    cont[x] = int(input(f'Digite o {x+1}º número: '))
    if cont[x] > mn:
        mn = cont[x]
    x = x+1
print('Os numeros digitados são ',cont,'\n')
print(f'O maior número é: {mn}')