import random
from time import sleep

print('-_--_-'*21)
print('                                         ADIVINHE O NUMERO QUE ESTOU PENSANDO')
print('-_--_-'*21)
n = random.randint(1,5)
chute = int(input('Em que número pensei?\n'))
print('PROCESSANDO...')
sleep(1.2)
if chute == n:
    print("Acertou mizeravi")
else:
    print(f'Não foi dessa vez {n}. \nTente novamente')
