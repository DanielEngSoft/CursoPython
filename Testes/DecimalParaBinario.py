'''      PRIMEIRA TENTATIVA
num = int(input('Digite o numero: '))
num2 = num
cont = 0
while num != 0:  # determinar quantos caracteres vai ter o numero binario
    cont = cont + 1
    num = int(num / 2)
x = [None] * cont
while cont > 0:
    x[cont - 1] = num2 % 2
    cont = cont - 1
    num2 = int(num2 / 2)
print(x)
'''
num = int(input('Digite o numero: '))
x = []
while num != 0:
    x.insert(0, num % 2)       # x.insert(0,) inclui na posiçao 0 da lista x o valor indicado após a virgula
    num = num // 2             # num recebe a divisão inteira de num por 2
result = ''                    # result é o caractere que vai substituir as virgulas da lista, somente por estética
print(result.join(map(str, x)))# map(,) transforma todos os elementos da lista no tipo escolhido

