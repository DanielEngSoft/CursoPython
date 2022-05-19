n = int(input('Digite quantos números da sequencia de fibonacci deseja ver: '))
c = 0
p1 = 0
p2 = p3 = 1
while c < n:
    print(f'{p1} ', end=' ')
    p1 = p2
    p2 = p3
    p3 = p1+p2
    c += 1
