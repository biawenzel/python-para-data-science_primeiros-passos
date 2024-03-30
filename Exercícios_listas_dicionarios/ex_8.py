'''8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.'''

doces = 0
amargos = 0
ids = []

for i in range(0, 10):
    ids.append(int(input(f'Digite o ID do {i+1}° produto: ')))


for id in ids:
    if id % 2 == 0:
        doces += 1
    else:
        amargos += 1
print(f'Lista de IDs: {ids}'
      f'\nQuantidade de produtos doces = {doces}' 
      f'\nQuantidade de produtos amargos = {amargos}')