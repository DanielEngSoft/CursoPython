SalarioAtual = float(input('Digite o salario atual do funcionário: '))
NovoSalario = SalarioAtual + SalarioAtual*0.15 if SalarioAtual <= 1250 else SalarioAtual + SalarioAtual * 0.10
print(f'O novo salário desse funcionário sera {NovoSalario} \n'
      f'Teve um aumento de R${NovoSalario-SalarioAtual}')
