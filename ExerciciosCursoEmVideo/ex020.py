import random
cont = 0
lista = [None] * 4
while cont < 4:
    lista[cont]=str(input(f'Digite o {cont+1}º nome: '))
    cont = cont + 1
random.shuffle(lista)
print(f'A sequencia escolhida foi:{lista}')