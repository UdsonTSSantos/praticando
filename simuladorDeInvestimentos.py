quanto = float(input('Informe o valor que deseja investir. R$ '))
print('Irá investir, R$', quanto ,'reais.\n'.upper())

anos = float(input('Por quantos anos deseja investir o valor informado. '))
if anos < 2:
  print('Precisa investir pelo tempo de no mínimo por 2 anos.\n'.upper())
  anos = float(input('Informe novamente por quanto tempo deseja investir\nlembrando que precisa ser no mínimo 2 anos.\n '))

perfil = str(input('Qual o seu perfil (M) moderado ou (A) agressivo, escolha M ou A. '.upper()))
if perfil == 'M':
   print('Seu perfil informado é Moderado, vamos ver quais investimentos temos par ao seu perfil.')
   print('Para esse perfil temos Selic - CDI - Tesouro direto. Gostou? ')
selic = 0.9
cdi = 0.5
tesouro = 0.10
print('Vamos ver as remunerações de cada investimento a partir do seu valor e tempo de investimento. ')
tempo = anos * 12
rselic = float(selic * quanto)
print(rselic)
print('Sua aplicação irá render por', tempo, 'meses', (selic * quanto) * tempo)

# Erro de cálculos