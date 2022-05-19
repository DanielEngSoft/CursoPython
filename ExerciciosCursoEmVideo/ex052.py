num = int(input('Digite um número:'))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(f'({c})', end=' ')
    else:
        print(c, end=' ')
if cont == 2 or cont ==1:
    print(f'\nO número {num} é divisivel apenas {cont}x, É um número primo')
else:
    print(f'\nO número {num} é divisivel {cont}x, NÃO é um número primo')