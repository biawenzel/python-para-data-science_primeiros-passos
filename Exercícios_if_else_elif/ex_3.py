#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input('Digite uma letra: ')
vogais = 'a, A, e, E, i, I, , o, O, u, U'

if letra in vogais:
  print (f'A letra {letra} é uma vogal')
else:
  print (f'A letra {letra} é uma consoante')