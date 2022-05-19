aluno = dict()
aluno['Nome'] = str(input('NOME: ')).strip().capitalize()
aluno['Media'] = float(input('MÉDIA: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} - {v}')

