altura=float(input('Digite aqui a sua altura em (m): '))
peso=float(input('Agora o seu peso em (Kg):'))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<=18.5:
    print('Abaixo do Peso')
elif imc<=25:
    print('Peso Ideal')
elif imc<=30:
    print('Sobrepeso')
elif imc<=40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
