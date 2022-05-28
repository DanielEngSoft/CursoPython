import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {p} é R${moeda.dobro(p):} ')
print(f'A metade de {p} é R${moeda.metade(p):} ')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10):} ')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13):} ')
