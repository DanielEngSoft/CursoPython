palavras = (
    'Aeiou',
    'Estrelas',
    'Juntar',
    'Falhar',
    'Dinamite',
    'Ampliar',
    'Poeira',
    'Vocais',
    'Alfaiate',
    'Laser',
    'Alemanha',
    'Vaqueiro',
    'Galinha',
    'Bruto',
    'Estrangeiro',
    'Maturidade',
    'Italiano',
    'Engrenagem',
    'Beisebol',
    'Nublado'

)
for p in sorted(palavras):
    print(f'\nNa palavra {p.upper()} temos ', end='-> ')
    for v in p:
        if v.lower() in 'aeiou':
            print(f'{v.upper()}', end=' ')
