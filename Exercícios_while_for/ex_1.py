'''1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.'''

num_1 = int(input('Digite o 1º numero: '))
num_2 = int(input('Digite o 2º numero: '))

if num_1 < num_2:
    while num_1 <= num_2:
        print(num_1)
        num_1 += 1
else:
    while num_2 <= num_1:
        print(num_2)
        num_2 += 1
