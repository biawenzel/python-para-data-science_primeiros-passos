#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
preco1 = float(input('Digite o preço do 1º produto: '))
preco2 = float(input('Digite o preço do 2º produto: '))
preco3 = float(input('Digite o preço do 3º produto: '))

mais_barato = preco1
if preco2 < mais_barato:
    mais_barato = preco2
if preco3 < mais_barato:
    mais_barato = preco3

print(f'O produto mais barato é o produto que custa R${mais_barato}')