num = []
cont = 0
while True:
    num.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').upper()
    if continuar == 'N':
        break

print(f'Valores digitados{cont:.>30}')
print(f'Decrescente: {sorted(num, reverse=True)}')
print('O valor 5 faz parte ' if 5 in num else 'O valor 5 não faz parte da lista')
