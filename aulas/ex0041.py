from datetime import date
atual= date.today().year
nasc=int(input('Digite aqui o ano de seu nascimento:'))
idade= atual-nasc
print('O atleta tem {} anos.'.format(idade))
if idade<= 9:
    print('De acordo com a sua idade, você entrará na categoria MIRIM')
elif idade<=14:
    print('De acordo com a sua idade, você entrará na categoria INFANTIL')
elif idade<=19:
    print('De acordo com a sua idade, você entrará na categoria JUNIOR')
elif idade<=25:
    print('De acordo com a sua idade, você entrará na categoria SÊNIOR')
else:
    print('De acordo com a sua idade, você entrará na categoria MASTER')









