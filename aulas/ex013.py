nome=input('Nome do Funcionário(a):')
sal=float(input('Digite aqui o salário inicial do funcionário R$='))
saf=sal+(sal*15)/100
print('O Salário do funcionário(a): {}, que inicialmente estava com R${:.3f}'.format(nome,sal),end= '')
print(', com 15% de aumento, passa a receber R$={:.2f} '.format( saf))


