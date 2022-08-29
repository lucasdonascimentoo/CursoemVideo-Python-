palavras=('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for p in palavras:
  print(f'\nNas palavras {p.upper()} temos ',end='')
  for letras in p:
    if letras.lower() in 'aeiou':
      print(letras,end='')