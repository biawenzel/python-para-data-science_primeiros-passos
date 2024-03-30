'''4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.'''

lista_numeros = []

for i in range(0, 5):
    num = int(input('Digite um número inteiro qualquer: '))
    lista_numeros.append(num)
lista_numeros.reverse()    
print(lista_numeros)