preco=float(input('Qual o preço do produto ?'))
print('''Qual a condição de pagamento ?
[1]À vista no dinheiro/cheque:10% de desconto
[2]À vista no cartão:5% de desconto
[3]Em até 2x no cartão:preço normal
[4]3x ou mais no cartão:20% de juros''')
opcao=int(input('Sua opção: '))
if opcao==1:
    total=preco-(preco*10/100)
    print('O valor a ser pago será R$={:.2f}'.format(total))
elif opcao==2:
    total=preco-(preco*5/100)
    print('O valor a ser pago em cartão será R$={:.2f}'.format(total))
elif opcao==3:
    total=preco/2
    print('O valor a ser pago em 2x no cartão será R$={:.2f} SEM JUROS'.format(total))
elif opcao==4:
    total= preco + (preco*20/100)
    totparc= int(input('Quantas parcelas ?'))
    parcela= total/totparc
    print('Sua compra será parcelada em {}x de R$={:.2f} COM JUROS'.format(totparc, parcela))
print('Sua compra de R$={:.2f} vai custar R${:.2f} no final'.format(preco, total))
