n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
print(f'Média de {media}\n')
if media >= 7.00:
    print('APROVADO!!')
elif media < 5:
    print('REPROVADO!!')
else:
    print('RECUPERAÇÃO!!')
