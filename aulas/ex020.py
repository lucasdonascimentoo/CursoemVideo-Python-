import random
print('NOMES DOS INTEGRANTES DO TRABALHO')
n1=str(input('Nome:'))
n2=str(input('Nome:'))
n3=str(input('Nome:'))
n4=str(input('Nome:'))
lista=[n1,n2,n3,n4]
ordem=random.shuffle(lista)
print('A ordem de apresentação será:{}'.format(lista))



