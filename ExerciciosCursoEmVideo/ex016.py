from math import trunc
############# PRIMEIRO JEITO  usando o int ###################
# n = float(input('Digite um valor'))
# x = 0
# x = int(n)
#
# print(f'O valor digitado é {n}, e sua parte inteira é {x}')
#
#
############# SEGUNDO JEITO / usando o Math.trunc ######################
n = float(input('Digite um valor'))
print(f'O valor digitado é {n}, e sua parte inteira é {trunc(n)}')