lista = []
a = 1
while a != 0:
    lista.insert(0, input(f'Digite o {len(lista)+1}º nome: '))
    if lista[0] == '':
        del lista[0]
        a = 0
lista.reverse()
print(lista)
