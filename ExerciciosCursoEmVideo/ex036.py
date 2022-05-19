vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$ '))
parcela = int(input('Digite quantos anos de financiamento: '))
vfin = vcasa / (parcela * 12)
print(f'Para pagar um financiamento de R${vcasa:.2f} em {parcela} anos,'
      f'a prestação será de R${vfin:.2f}')
if vfin > salario * 0.30:
    print('Emprestimo NEGADO!!!')
else:
    print('Emprestimo APROVADO!!!')
