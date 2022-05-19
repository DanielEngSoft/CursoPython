hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
r = []
num = int(input('Digite um número: '))
while num != 0:
    r.insert(0, hexa[num % 16])
    num = num // 16
a = ''
print(a.join(map(str, r)))