n1 =int(input('Digite o primeiro valor: '))
n2 =int(input('Digite outro valor: '))
n3 =int(input('Digite o terceiro valor: '))
n4 =int(input('Digite o ultimo valor: '))
lista = (n1, n2, n3, n4)
print(f'o número 9 apareceu {lista.count(9)}x')
if 3 in lista:
    print(f'o número 3 apareceu pela primeira vez na posição {lista.index(3)+1}')
else:
    print('Não tem o número 3 na lista')
print('Os numeros pares digitados foram:', end=' ')
cont = 0
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
        cont += 1
if cont == 0:
    print('NENHUM NÚMERO PÁR DIGITADO')