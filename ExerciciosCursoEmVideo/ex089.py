from time import sleep
lista = []
notas = []
cont = 1
while True:
    media = 0
    nome = str(input(f'Aluno {cont}: ')).strip().capitalize()
    for n in range(1, 3):
        notas.append(float(input(f'NOTA {n}: ')))
    media = (notas[0] + notas[1])/2
    lista.append([nome, notas[:], media])
    notas.clear()
    cont += 1
    if input('CONTINUAR? [S/N]').strip().upper()[0] == 'N':
        break
print(lista)
print('.' * 60)
print(f'|{"Nº":<4}|{"NOME":^25}|{"MÉDIA":>8}|')
for l in range(0, len(lista)):
    print(f'|{l:<4}|{lista[l][0]:^25}|{lista[l][2]:>8.2f}|', end='  ')
    print('APROVADO    |' if lista[l][2] >= 7 else 'RECUPERAÇÃO |')
print('.' * 60)
while True:
    dadosDoAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if dadosDoAluno == 999:
        print(f'{"VOLTE SEMPRE":-^60}')
        break
    elif 0 <= dadosDoAluno < len(lista):
        print(f'ALUNO: {lista[dadosDoAluno][0]} \nNOTAS:{lista[dadosDoAluno][1]}')
        sleep(2)
    else:
        print('ALUNO NÃO ENCONTRADO!!!')
        sleep(2)