'''3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].'''

lista_numeros = []

for i in range(0, 5):
    num = int(input('Digite um número inteiro qualquer: '))
    lista_numeros.append(num)
print(lista_numeros)