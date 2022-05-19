print('------FATORIAL------')
num = int(input('Digite o número que deseja saber seu fatorial: '))
f = num
cont = num-1
print(f'{f}! = {f}',end='')
while cont > 0:
    num *= cont
    cont -= 1
    if cont != 0:
        print(f' x {cont}', end='')
print(f' = {num}')