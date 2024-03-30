'''5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.'''

num = int(input('Digite o número: '))
lista_primos = []

for i in range(2, num):
    primo = True
    for divisiveis in range (2, i):
        if i % divisiveis == 0:
            primo = False
            break
    if primo == True:
        lista_primos.append(i)

print(f'Lista de números primos de 1 até {num}: {lista_primos}')
