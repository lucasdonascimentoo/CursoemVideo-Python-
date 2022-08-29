'''import math
co=float(input('Digite aqui o comprimento do cateto oposto do seu triângulo retângulo:'))
ca=float(input('Agora o cateto adjacente:'))
h=pow(co,2)+pow(ca, 2)
ah=math.sqrt(h)
print('A hipotenusa vai medir:{:.2f}'.format(ah))'''
#ou
import math
co=float(input('Cateto opostoo:'))
ca=float(input('Cateto adjacente:'))
hi=math.hypot(co, ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))


