dias = int(input('Quantos dias alugados:'))
km = int(input('Digite os km percorridos:'))
p = (km*0.15) + (dias*60)
print('O valor a pagar é de {:.2f}'.format(p))