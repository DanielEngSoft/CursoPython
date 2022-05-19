soma = 0
cont = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Foi digitado {cont} números pares, e a soma é {soma}')
