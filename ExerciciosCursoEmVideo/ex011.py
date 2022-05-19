l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
mq = l*a
print('Para uma parede de {}m², você irá precisar de {:.2f} litros de tinta!'.format(mq, mq/2))
