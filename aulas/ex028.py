from random import randint
from time import sleep
computador= randint(0, 5) #Faz o computador 'Pensar'
print('~'*57)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('~'*57)
jogador= int(input('Em que número eu pensei ? ')) #o jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você acertou !!')

else:
    print('ERRRRRRRRRRROU !')

print('Eu pensei no número {}'.format(computador))
