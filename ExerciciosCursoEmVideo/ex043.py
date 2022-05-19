peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
tx = 'Seu estado atual é de '
if altura > 18:
    altura = altura/100
imc = peso / (altura*altura)

print('''\n\n–-- IMC abaixo de 18,5: Abaixo do Peso
–-- Entre 18,5 e 25: Peso Ideal
–-- 25 até 30: Sobrepeso
–-- 30 até 40: Obesidade
–-- Acima de 40: Obesidade Mórbida\n\n''')
print(f'Seu imc é de {imc:.2f}')
if imc < 18.5:
    print(f'{tx}ABAIXO DO PESO!')
elif imc <= 25:
    print(f'{tx}PESO IDEAL!')
elif imc < 30:
    print(f'{tx}SOBREPESO!')
elif imc < 40:
    print(f'{tx}OBESIDADE!')
else:
    print(f'{tx}OBESIDADE MÓRBIDA!')