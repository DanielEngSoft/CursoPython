import math
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
#h = math.sqrt(math.pow(c1,2) + math.pow(c2,2))
h = math.hypot(c1,c2)
print(f'A hipotenusa vale {h:.2f}')
