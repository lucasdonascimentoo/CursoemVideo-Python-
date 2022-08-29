qd=int(input('Quantos dias o carro foi alugado?'))
qk=float(input('Quantos km foram rodados ?'))
pagar=(qd*60) + (qk*0.15)
print('O total a pagar é de R${:.2f}'.format(pagar))

