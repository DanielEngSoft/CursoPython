inicio: int = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
tamanhoPA = 10
while c < tamanhoPA:
    print(inicio, end='  ')
    inicio += razao
    c += 1
    if c == tamanhoPA:
        tamanhoPA += int(input('\nQuer mostrar mais quantos termos? '))
print(f'ACABOU\nVoce mostrou {c} termos no final')
