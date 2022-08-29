n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda: '))
m=(n1+n2)/2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2,m))
if m<5:
    print('REPROVADO!')
elif 5<m<6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')




