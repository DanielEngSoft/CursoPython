import math
a = int(input('Digite o angulo que você deseja: '))
sa = math.sin(math.radians(a))
ca = math.cos(math.radians(a))
ta = math.tan(math.radians(a))
print(f'SENO = {sa:.2f}\nCOSENO = {ca:.2f}\nTANGENTE = {ta:.2f}')