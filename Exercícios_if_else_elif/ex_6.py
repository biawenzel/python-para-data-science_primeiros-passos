#6) Escreva um programa que leia três números e os exiba em ordem decrescente.
num_1 = int(input('Digite o 1º número: '))
num_2 = int(input('Digite o 2º número: '))
num_3 = int(input('Digite o 3º número: '))

if (num_1 >= num_2) and (num_1 >= num_3):
    print(num_1)
    if num_2 >= num_3:
        print(num_2)
        print(num_3)
    else:
        print(num_3)
        print(num_2)
elif (num_2 >= num_1) and (num_2 >= num_3):
    print(num_2)
    if num_3 >= num_3:
        print(num_1)
        print(num_3)
    else:
        print(num_3)
        print(num_1)
else:
    print(num_3)
    if num_1 >= num_2:
        print(num_1)
        print(num_2)
    else:
        print(num_2)
        print(num_1)
