#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num_1 = int(input('Digite o 1º número: '))
num_2 = int(input('Digite o 2º número: '))

if num_1 > num_2:
  print(f'{num_1} é o maior número')
else:
  print(f'{num_2} é o maior número')