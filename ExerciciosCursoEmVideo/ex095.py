jogador = {}
jogadores = list()
# ----------------------LENDO OS DADOS--------------------- #
while True:
    jogador['Nome'] = input('Nome do jogador: ').strip().capitalize()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas = []
    for p in range(0, jogador['Partidas']):
        partidas.append(int(input(f'--Quantos gols na {p + 1}ª partida? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas[:])
    jogadores.append(jogador.copy())
# ----------------------CONTINUAR OU NÃO--------------------- #
    while True:
        continuar = input('Quer continuar? [S/N]').upper().strip()[0]
        if continuar in 'NS':
            break
        else:
            print('ERRO!! Digite apenas S ou N!')
    if continuar == 'N':
        break
# ----------------------MOSTRANDO OS DADOS 1--------------------- #
#print('--' * 35, '\n', jogadores, '\n', '--' * 35)
# ----------------------MOSTRANDO OS DADOS 2--------------------- #
print('--' * 35)
print(f"{'Cód':<4}| {'Nome':<20}| {'Gols':<30}| {'Total':<3}")
for c, i in enumerate(jogadores):
    print(f"{c:>4}| {i['Nome']:<20}| {str(i['Gols']):<30}| {i['Total']:<3}")
print('--' * 35)
# ----------------------MOSTRANDO OS DADOS 3--------------------- #
while True:
    opcMenu = int(input('Mostrar dados de qual jogador? (999 para sair)'))
    if 0 <= opcMenu < len(jogadores):
        print(f'{jogadores[opcMenu]["Nome"].upper():-^35}')
        for gol in range(0, jogadores[opcMenu]['Partidas']):
            print(f'--Na {gol + 1}ª partida fez {jogadores[opcMenu]["Gols"][gol]} gol(s).')
    elif opcMenu == 999:
        break
    else:
        print('Jogador não encontrado!!')