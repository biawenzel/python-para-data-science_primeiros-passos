'''4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.'''

temperatura = float(input('Digite uma temperatura em °C: '))
qtds = 0
soma = 0

while temperatura != -273:
    soma += temperatura
    qtds += 1
    temperatura = float(input('Digite uma temperatura em °C: '))
media = soma/qtds
print(f'A média das temperaturas é: {media} ')
