pessoasTemp = dict()
pessoas = list()
listaF = list()
mediaidade = 0
while True:
    pessoasTemp['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoasTemp['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoasTemp['Sexo'] not in 'MF':
            print('ERRO!! Digite apenas M ou F!')
        else:
            break
    if pessoasTemp['Sexo'] == 'F':
        listaF.append(pessoasTemp['Nome'])
    pessoasTemp['Idade'] = int(input('Idade: '))
    mediaidade += pessoasTemp['Idade']
    pessoas.append(pessoasTemp.copy())
    continuar = ' '
    while True:
        continuar = input('Quer continuar? [S/N]').upper().strip()[0]
        if continuar in 'NS':
            break
        else:
            print('ERRO!! Digite apenas S ou N!')
    if continuar == 'N':
        break
print(pessoas)
mediaidade /= len(pessoas)
print('-='*23)
print(f'A- Ao todo temos {len(pessoas)} cadastradas.')
print(f'B- A méadia de idade é de {mediaidade} anos.')
print(f'C- As mulheres cadastradas foram {listaF}.')
print(f'D- Lista de pessoas que estão acima da média:')
for i in pessoas:
    if i['Idade'] > mediaidade:
        print('  ', end='')
        for k, v in i.items():
            print(f"{k} - {v}", end="; ")
        print()
