'''11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
Escreva um código que calcule o total de vendas e o produto mais vendido.'''

vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = 0
mais_vendido = ''
qtd_mais_vendido = 0

for qtd in vendas.values():
    total_vendas += qtd
print(f'Total de vendas = {total_vendas}')

for i in vendas.keys():
    if vendas[i] > qtd_mais_vendido:
        qtd_mais_vendido = vendas[i]
        mais_vendido = i
print(f'O produto mais vendido é {mais_vendido}')