dis=float(input('Digite aqui a distância de sua viagem em KM: '))
if dis<= 200:
    ps=0.50*dis
    print('O valor que você terá q pagar de passagem será R$:{:.2f}'.format(ps))
else:
    ps2=0.45*dis
    print('O valor que você pagará de passagem será R$:{:.2f}'.format(ps2))
