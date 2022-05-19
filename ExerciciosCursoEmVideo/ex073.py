times = ('Corinthians', 'América-MG', 'Bragantino', 'Atlético-MG',
         'Coritiba', 'São Paulo', 'Santos', 'Cuiabá', 'Internacional', 'Avaí',
         'Athletico-PR', 'Flamengo', 'Botafogo', 'Palmeiras', 'Fluminense',
         'Ceará SC', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')

for c in range(0, 20):
    print(f'{c+1:<2}º{times[c]:.>20}')

print(f'\nOs 5 primeiros são: {times[:6]}')
print(f'Os 4 ultimos são: {times[-4:]}')
print('Ordem alfabética:', end=' ')
print(sorted(times))
print(f'O Flamengo atualmente está na {times.index("Flamengo")+1}ª colocação')
