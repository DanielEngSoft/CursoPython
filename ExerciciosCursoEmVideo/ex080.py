lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        print('Adicionado ao final da lista')
    else:
        if lista[c] > lista[c-1]:
            print('Adicionado ao final da lista')
        else:
            for p in range(0, c):
                if lista[c] < lista[p]:
                    lista.insert(p, lista[c])
                    lista.pop()
                    print(f'Adicionado na posição {p}')
                    break
print('-'*35)
print('Os valores digitados em ordem foram', lista)
