lista = []
listaPar = []
listaImpar = []
while True:
    lista.insert(0, int(input('Digite um valor: ')))
    if lista[0] % 2 == 0:
        listaPar.insert(0, lista[0])
    else:
        listaImpar.insert(0, lista[0])
    if input('Deseja continuar? [S/N]').upper()[0] == 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista Par: {listaPar}')
print(f'Lista Impar: {listaImpar}')
