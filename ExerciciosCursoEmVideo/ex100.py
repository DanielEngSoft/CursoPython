from random import randint
from time import sleep


def Sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    lista = list()
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(lista[c], end=' ')
        sleep(0.3)
    print('PRONTO!')
    return lista


def SomaPar(lista):
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Somando os valores pares de {lista}, temos {soma}')
    return soma


lista = Sorteia()
SomaPar(lista)
