nome=str(input('Nome do aluno(a): '))
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=7:
    print('Parabéns {}, você está na média !'.format(nome))

else:
    print('Você terá que se esforçar mais para atingir a média !')

