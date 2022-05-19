lista = list()
for c in range(0, 10):
    lista.append(int(input(f'Valor da posição {c}: ')))
maior = max(lista)
menor = min(lista)

print(f'Maior -> {maior}\n'
      f'Menor -> {menor}')
print('Posição do maior: ', end=' ')
for c, v in enumerate(lista):
    if v == maior:
        print(c, end=' ')
print('\nPosição do menor: ', end=' ')
for c, v in enumerate(lista):
    if v == menor:
        print(c, end=' ')
