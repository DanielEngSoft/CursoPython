from operator import itemgetter
from time import sleep
from random import randint
jogadores = {}
for c in range(1, 5):
    nome = input(f'Nome do {c}º jogador: ').strip().capitalize()
    jogadores[nome] = randint(1, 6)
print(f'{"Valores sorteados":-^60}')
for k, v in jogadores.items():
    print(f'{k} com {v}')
    sleep(0.8)
rank = []
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
for k, v in enumerate(rank):
    print(f'{k+1}º - {v[0]} tirou {v[1]}')
print(rank)
