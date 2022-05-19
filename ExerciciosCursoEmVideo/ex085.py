num = [[], []]
for c in range(0, 7):
    num[0].insert(0, int(input(f'Digite o {c+1}º valor: ')))
    if num[0][0] % 2 == 1:
        num[1].append(num[0][0])
        num[0].pop(0)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')
