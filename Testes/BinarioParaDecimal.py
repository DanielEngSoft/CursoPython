'''a = 0
binario = 0
cont = 0

num = int(input('Digite o numero binario: '))
while num > 0:
    a = num % 2 se for inpar vai ser 1, se for par é zero
    binario += a * 2 ** cont
    num = num // 10
    cont += 1
print(binario)'''


''' Jeito ensinado pelo professor Pierre, jeito facio de entender
r = 0
cont = 0
num = str(input('Digite o numero binario: '))
a = len(num)
while a > 0:
    r = r + int(num[a - 1]) * 2 ** cont
    cont += 1
    a -= 1
print(r)
'''

r = 0
cont = 0
a = 0
num = str(input('Digite o numero binario: '))

while a < len(num):
    r = (2 * r) + int(num[a])
    a += 1
print(r)
'''
num = int(input('Digide um numero binário: '))
print(int(num, 2))
'''