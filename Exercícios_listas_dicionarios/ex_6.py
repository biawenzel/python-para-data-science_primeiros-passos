'''6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.'''

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2:
    #verificação se o ano é bissexto
    if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
        dias_fevereiro = 29
    else:
        dias_fevereiro = 28
    
    if 1 <= dia <= dias_fevereiro:
        print(f'A data {dia}/{mes}/{ano} é válida')
    else:
        print(f'Não existe dia {dia} em fevereiro no ano {ano}, portanto, a data é inválida')
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        print(f'A data {dia}/{mes}/{ano} é válida')
    else:
        print(f'A data {dia}/{mes}/{ano} é inválida')
else:
    print(f'A data {dia}/{mes}/{ano} é inválida')
