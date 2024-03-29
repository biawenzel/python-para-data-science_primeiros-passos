'''8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.'''

idade = int(input('Informe a idade (ou um número negativo para encerrar): '))
grupo_1 = 0
grupo_2 = 0
grupo_3 = 0
grupo_4 = 0

while idade > 0:
    if 0 < idade <= 25:
        grupo_1 += 1
    elif 25 < idade <= 50:
        grupo_2 += 1
    elif 50 < idade <= 75:
        grupo_3 +=1
    elif 75 < idade <= 100:
        grupo_4 +=1
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))
print(f'[0-25]: {grupo_1} \n[26-50]: {grupo_2} \n[51-75]: {grupo_3} \n[76-100]: {grupo_4}')