def ficha(nome='<NÃO INFORMADO>', gols=0):
    print(f'Jogador {nome} fez {gols} no campeonato')


#programa principal
n = str(input('NOME DO JOGADOR: ')).strip().capitalize()
g = str(input('Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
