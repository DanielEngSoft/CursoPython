def notas(*num, sit=False):
    """
    -> Função para analizar e mostrar situação de cada aluno
    :param num: TODAS AS NOTAS
    :param sit: (OPCIONAL) CASO TRUE MOSTRA COMO ESTÁ A MÉDIA DO ALUNO
    :return: RETORNA UMA BIBLIOTECA COM TODOS OS DADOS DO ALUNO
    """
    dados = dict()
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    dados['Media'] = sum(num) / len(num)
    if sit:
        if dados['Media'] >= 7:
            dados['Situação'] = 'BOA'
        elif dados['Media'] >= 5:
            dados['Situação'] = 'BOA'
        else:
            dados['Situação'] = 'RUIM'
    return dados


resp = notas(5, 10, 4, 6, 4.5, 8, sit=True)
print(resp)
