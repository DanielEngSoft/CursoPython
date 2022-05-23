from datetime import date


def voto(id):
    if id < 18:
        resp = 'NÃO VOTA'
    elif id < 65:
        resp = 'VOTO OBRIGATORIO'
    else:
        resp = 'VOTO OPCIONAL'
    return resp


i = int(input('Ano de nascimento: '))
idade = date.today().year - i
print(f'COM {idade} ANOS: {voto(idade)} ')
