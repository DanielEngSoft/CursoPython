cidade = 'SANTO'
x = str(input('Em que cidade você nasceu?')).upper().strip()
separa = x.split()
print(cidade in separa[0])
