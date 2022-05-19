lado1 = float(input('Digite o primeiro segmento: '))
lado2 = float(input("Digite o segundo segmento: "))
lado3 = float(input('Digite o terceiro segmento: '))
possivel = 'é possivel formar um triangulo com esses segmentos!'
if lado1 > lado2 + lado3:
    print('Não', possivel)
elif lado2 > lado1 + lado3:
    print('Não', possivel)
elif lado3 > lado1 + lado2:
    print('Não', possivel)
else:
    print('Sim,',possivel)