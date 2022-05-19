import datetime
from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['Idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposenta'] = pessoa['Contratação'] + pessoa['Idade'] - date.today().year + 35
for k, v in pessoa.items():
    print(f'-- {k}: {v}')
