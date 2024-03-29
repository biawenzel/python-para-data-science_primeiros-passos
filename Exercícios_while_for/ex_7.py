'''7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''

num = int(input('Digite o número: '))

primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break

if primo == True:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')