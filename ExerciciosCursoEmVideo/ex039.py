import datetime
gen = input('Digite seu genero: M para Masculino e F para Feminino\n').strip().upper()
if gen == 'M':
    idade = datetime.date.today().year - int(input('Digite seu ano de nascimento: '))
    if idade == 18:
        print('Está no Ano de se alistar')
    elif idade < 18:
        print(f'Falta {18-idade} ano(s) para seu alistamento ')
    else:
        print(f'Passou {idade - 18} ano(s) do seu alistamento ')
elif gen == 'F':
    print('O serviço militar não é obrigatorio')
else:
    print('Opção invalida')