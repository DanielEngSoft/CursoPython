def Area(l, c):
    area = l*c
    print(f'A áreade um terreno {l}m x {c}m é de {area}m²')


print(f'{"CONTROLE DE TERRENO":-^40}')
c = float(input('COMPRIMENTO (m): '))
l = float(input('LARGURA (m): '))
Area(l, c)
