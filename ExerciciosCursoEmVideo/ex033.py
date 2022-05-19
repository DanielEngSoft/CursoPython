''''#### Cria uma lista
numeros = []
#### Adiciona valores a lista
for i in range(0,10):
    numeros.append(int(input(f'Digite o {i+1}º valor: ')))
#### Escolhe um valor da lista e atribui ao maior e menor valor
maior = numeros[0]
menor = numeros[0]
#### Compara os valores escolhidos com os outros
for i in range(0, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
#### Mostra os valores
print(f'O maior numero é {maior}\nO menor numero é {menor}')'''
numeros = []
for i in range(0,10):
    numeros.append(int(input(f'Digite o {i+1}º valor: ')))
print(f'O maior numero é {max(numeros[0:])}\nO menor numero é {min(numeros[0:])}')