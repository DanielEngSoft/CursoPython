nomes = []              #cria uma lista para os nomes
idades = []             #cria uma lista para idades
sexos = []              #cria uma lista para os sexos
Media_Idades = 0        #variável para calcular a média das idades
IdadeHomemMaisVelho = 0 #variável para saber a idade do sexo 'H' de maior valor
MulherMenorVinte = 0    #variável para somar quantas variaveis com valor 'F' são menores que 20
NomeHomemMaisVelho = '' #variável para saber quem é o homem mais velho
for c in range(0,4):
    print(f'------ {c+1}ª PESSOA ------')
    nomes.append(input('NOME: ').strip().capitalize())      #   \
    sexos.append(input('SEXO [M/F]: ').strip().upper())     #    --->Atualiza o valor das listas na posição c
    idades.append(int(input('IDADE: ')))                    #   /
    Media_Idades += idades[c]                           #Media_Idade soma ela mesma mais a Idade da posição c
    if sexos[c] == 'M' and idades[c] > IdadeHomemMaisVelho:
        IdadeHomemMaisVelho = idades[c]
        NomeHomemMaisVelho = nomes[c]                   #
    elif sexos[c] == 'F' and idades[c] < 20:
        MulherMenorVinte += 1

Media_Idades /= 4
print(f'A média de idade do grupo é de {Media_Idades}')
if IdadeHomemMaisVelho != 0:
    print(f'O homem mais velho tem {IdadeHomemMaisVelho} anos e se chama {NomeHomemMaisVelho}')
else:
    print('Não temos Homens na lista')
print(f'Ao todo são {MulherMenorVinte} mulhere(s) com menos de 20 anos')
