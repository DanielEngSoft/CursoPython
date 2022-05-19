jogador = {}
jogador['Nome'] = input('Nome do jogador: ').strip().capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
partidas = []
for p in range(0, jogador['Partidas']):
    partidas.append(int(input(f'--Quantos gols na {p+1}ª partida? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas[:])
print('-='*35, '\n', jogador, '\n', '-='*35)
for k, v in jogador.items():
    print(f'{k} == {v}')
print('-='*35)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Total"]} partidas.')
for p in range(0, len(partidas)):
    print(f'--Na {p+1}ª partida fez {partidas[p]} gol(s).')
print(f'Foi um total de {jogador["Total"]} gol(s)')
