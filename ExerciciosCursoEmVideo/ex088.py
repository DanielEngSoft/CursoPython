from random import randint
print('-'*40)
print(f"|{'Gerador de Números':^38}|")
print('-'*40)

njogos = int(input('JOGOS A SEREM SORTEADOS: '))

jogosTemp = []
jogos = []
for t in range(0, njogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogosTemp:
            jogosTemp.append(num)
            cont += 1
        if cont == 6:
            print(sorted(jogosTemp))
            break
    jogos.append(sorted(jogosTemp[:]))
    jogosTemp.clear()
print(f'{f"BOA SORTE":-^40}')