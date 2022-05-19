import datetime

texto = 'E está na categoria '
idade = datetime.date.today().year - int(input('Digite o ano de nascimento do atleta: '))
print(f'O atleta tem {idade} anos')
if 0 < idade <= 9:
    print(f'{texto}MIRIM')
elif idade <= 14:
    print(f'{texto} INFANTIL')
elif idade <= 19:
    print(f'{texto} JUNIOR')
elif idade <= 25:
    print(f'{texto} SÊNIOR')
else:
    print(f'{texto} MASTER')