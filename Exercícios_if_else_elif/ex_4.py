#4) Escreva um programa que leia valores médios de preços de um modelo de carro
# por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
preco_ano_1 = int(input('Digite o 1º valor: '))
preco_ano_2 = int(input('Digite o 2º valor: '))
preco_ano_3 = int(input('Digite o 3º valor: '))

maior = preco_ano_1
if preco_ano_2 > maior:
  maior = preco_ano_2
if preco_ano_3 > maior:
  maior = preco_ano_3

menor = preco_ano_1
if preco_ano_2 < menor:
  menor = preco_ano_2
if preco_ano_3 < menor:
  menor = preco_ano_3

print(f'O preço mais alto foi de R${maior}.')
print(f'O preço mais baixo foi de R${menor}.')