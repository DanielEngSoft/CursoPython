nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
media = (nt1 +nt2)/2
print('A media do aluno é: {}'.format(media))
if media >= 7:
    print('Aprovado!!')
else:
    print('Reprovado')