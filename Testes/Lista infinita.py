n = int(input('Digite quantos nomes quer adicionar a lista: '))
cont = 0
lista = [None] * n
while cont < n:
    lista[cont] = input(f'Digite o {cont+1}º nome: ')
    cont = cont + 1
x = int(input('Digite a posição da lista que deseja ver o nome: '))
print(lista[x-1])