def voto(nasc):
    """
    :param nasc: ANO DE NASCIMENTO, USADO PARA CALCULAR A IDADE
    :return: RETORNA SE A PESSOA VOTA OU NÃO
    """
    from datetime import date
    id = date.today().year - nasc
    if id < 16:
        resp = 'NÃO VOTA'
    elif 16 < id > 65:
        resp = 'VOTO OPCIONAL'
    else:
        resp = 'VOTO OBRIGATORIO'
    return f'Com {id} anos: {resp}'


anoNascimento = int(input('Ano de nascimento: '))
print(voto(anoNascimento))
