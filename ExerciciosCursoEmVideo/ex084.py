lista = []
dados = []
pessoasP = []
pessoasL = []
while True:
    dados.append(input('Nome: ').capitalize().strip())
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maiorP = menorP = dados[1]
    else:
        if dados[1] > maiorP:
            maiorP = dados[1]
        if dados[1] < menorP:
            menorP = dados[1]
    lista.append(dados[:])
    dados.clear()
    if input('Quer continuar? [S/N]').strip().upper()[0] == 'N':
        break
print(lista)
for c in lista:
    if c[1] == maiorP:
        pessoasP.append(c[0])
for c in lista:
    if c[1] == menorP:
        pessoasL.append(c[0])
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maiorP}Kg. Peso de {pessoasP}')
print(f'O menor peso foi de {menorP}Kg. Peso de {pessoasL}')
