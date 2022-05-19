Mais18 = 0
homens = 0
m20 = 0
cont = 1
while True:
    sexo = sair = ' '
    idade = int(input(f'Digite a idade da {cont}ª pessoa: '))
    while sexo not in('MF'):
        sexo = str(input(f'Digide o sexo da {cont} pessoa [M/F]: ')).strip().upper()
    if idade > 18:
        Mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    while sair not in ('SN'):
        sair = str(input('Deseja continuar? [S/N]')).strip().upper()
    if sair == 'N':
        break
    cont += 1
print(f'Pessoas maiores de 18: {Mais18:.>17}\n'
      f'Homens cadastrados: {homens:.>20}\n'
      f'Mulheres com mais de 20 anos: {m20:.>10}')
