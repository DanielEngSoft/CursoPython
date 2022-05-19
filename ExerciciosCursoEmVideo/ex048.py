soma = 0
cont = 0
for c in range(0, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma dos {cont} numeros ímpares divisiveis por 3 entre 1 e 500 é {soma}')
