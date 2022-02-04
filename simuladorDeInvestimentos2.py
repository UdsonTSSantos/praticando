valor = float(input('Informe o valor que deseja investir todo mês. R$ '))
if valor <= 9:
  print('O valor mínimo de investimento mês precisa ser de R$ 20,00 - O valor que informou não está dentro do valor mínimo.'.upper())
  print('Vamos tentar novamente.')
  valor = float(input('Informe novamente o valor que deseja investir, lembre-se que não pode ser inferior á R$ 20,00\n '))
  if valor <= 9:
    print('Valor não atingiu o valor mínimo, um de nossos consultores irá lhe orientar em até 24 horas por telefone.\n ')
    

tempo = float(input('Por quanto tempo pretende deixar o valor investido? Informe em anos. '))
meses = tempo * 12
print('Confirmando, investir R$', valor, 'por', int(meses), ' meses, vamos denominador seu perfil de investidor.'.upper())

tipo = input('Qual é seu perfil de investidor (M) Moderado ou (A) Agressivo? Escolha M ou A. ').upper()
if tipo == 'M':
  print('Perfil moderado, vamos relacionar quais investimentos par ao seu perfil e os ganhos. ')
  print('Onde investir moderadamente? Tesoura - CDI - CDB eles vão render até 2% ao mês, vamos simular os valores a partir do tempo que informou.')
  rental = (valor * 0.02) * meses
  print('Durante', int(tempo), 'ano(s) investindo R$', valor, ' terá no final R$', (rental + valor) * meses)
  print('Rentabilidade valor investido x 2% x tempo = R$', rental, '| Tempo de investimento', int(meses), 'meses | Valor investido por mês R$', valor)
else:
  print('Precisa informar apenas as iniciais (M) para moderado ou (A) para agressivo.')
