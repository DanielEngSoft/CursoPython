import datetime
maior = 0
menor = 0
for c in range(0, 7):
    idades = int(input(f'Digite em que ano a {c+1}ª pessoa nasceu: '))
    if datetime.date.today().year - idades >= 18:
        maior += 1
    else:
        menor += 1
print(f'\nAo todo tivemos {maior} pessoas maiores de idade')
if menor > 0:
    print(f'E tambem tivemos {menor} pessoas menores de idade')
