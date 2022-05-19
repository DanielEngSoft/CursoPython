'''lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if len(lista) == 1:
        print('Valor adicionado com sucesso!')
    else:
        if lista[len(lista)-1] in lista[0:-1]:
            lista.pop()
            print('Valor ja existe, não será adicionado!')
        else:
            print('Valor adicionado com sucesso!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break

print(f'Você digitou os valores: {sorted(lista)}')

'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if lista[len(lista)-1] not in lista[0:-1]:
        print('Valor adicionado com sucesso!')
    else:
        lista.pop()
        print('Valor ja existe, não será adicionado!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break

print(f'Você digitou os valores: {sorted(lista)}')