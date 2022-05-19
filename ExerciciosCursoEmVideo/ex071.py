print(f'{" Banco D¢$ ":=^30}')
notas = (100, 50, 20, 10, 5, 2, 1)
quant_notas = [0, 0, 0, 0, 0, 0, 0]
cont = 0
valor = int(input('Digite o valor a ser sacado: '))
while valor > 0:
    if valor >= notas[cont]:
        valor -= notas[cont]
        quant_notas[cont] = quant_notas[cont] + 1
        if valor < notas[cont]:
            print(f'Notas de R${notas[cont]:>2} {quant_notas[cont]:.>16}')
    else:
        cont += 1
