dis = float(input('Qual a distância da sua viajem? '))
custo = 0
if dis <= 200:
    custo = dis * 0.5
else:
    custo = dis * 0.45
print(f'Você está prestes a começar uma viajem de {dis:.2f}km!\n'
      f'E o preço da sua passagem será de R${custo:.2f}')
