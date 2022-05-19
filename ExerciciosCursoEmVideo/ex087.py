matriz = [[], [], []]
soma = 0
somaC3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somaC3 += matriz[l][c]
print('-_'*15)
for l in range(0, 3):
    print(' '*8, end='')
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()
print('-_'*15)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira é {somaC3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
