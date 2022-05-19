velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado!! Você exedeu o limite de 80km/h')
    print(f'Você deve pagar uma multa de R${(velocidade-80)*7:.2f}')
print('boa tarde')


