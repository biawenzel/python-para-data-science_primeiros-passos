'''12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

- O valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
- O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.'''

tipo = input('Qual tipo do combustível? (E - etanol / D - diesel): ')
qtd_litros = float(input('Quantos litros foram abastecidos? '))
preco_e = 1.7
preco_d = 2.0

if tipo == 'E' or tipo == 'e':
    if qtd_litros < 0.0:
        print('A quantidade de litros deve ser um valor maior que 0.')
    elif 0.0 < qtd_litros <= 15.0:
        total = preco_e * qtd_litros - (preco_e * qtd_litros * 0.002)  
        print(f'O total é de R${total}')      
    elif qtd_litros > 15.0:
        total = preco_e * qtd_litros - (preco_e * qtd_litros * 0.004)
        print(f'O total é de R${total}')
elif tipo == 'D' or tipo == 'd':
    if qtd_litros < 0.0:
        print('A quantidade de litros deve ser um valor maior que 0.')
    elif 0.0 < qtd_litros <= 15.0:
        total = preco_d * qtd_litros - (preco_d * qtd_litros * 0.003)
        print(f'O total é de R${total}')
    elif qtd_litros > 15.0:
        total = preco_d * qtd_litros - (preco_d * qtd_litros * 0.005)
        print(f'O total é de R${total}')
elif tipo != 'E' or tipo != 'e' or tipo != 'D' or tipo != 'd':
    print('Insira um tipo de combustível válido (E ou D).')