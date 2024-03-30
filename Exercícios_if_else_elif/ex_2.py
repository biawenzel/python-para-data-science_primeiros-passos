#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e
# informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
percent = float(input('Digite o percentual de crescimento de produção da empresa: '))

if percent < 0.0:
  print('Houve decrescimento')
else:
  print('Houve crescimento')