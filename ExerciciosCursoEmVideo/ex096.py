def Area(largura, comprimento):
    area = largura * comprimento
    print(f'A áreade um terreno {largura}m x {comprimento}m é de {area}m²')


print(f'{"CONTROLE DE TERRENO":-^40}')
c = float(input('COMPRIMENTO (m): '))
l = float(input('LARGURA (m): '))
Area(l, c)
