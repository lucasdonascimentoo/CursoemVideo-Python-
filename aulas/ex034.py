sal=float(input('Informe aqui o seu sálario atual R$: '))
if sal<=1250:
    novo=sal +(sal*15/100)
else:
    novo=sal +(sal*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, novo))

