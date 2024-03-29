'''10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ela deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.'''
num_1 = float(input('Digite o 1º número: '))
oper = input('Qual operação deseja realizar? (Digite +, -, * ou /): ')
num_2 = float(input('Digite o 2º número: '))

if oper == '+':
    resultado = num_1 + num_2
    print(f'O resultado da operação é {resultado}')
elif oper == '-':
    resultado = num_1 - num_2
    print(f'O resultado da operação é {resultado}')
elif oper == '*':
    resultado = num_1 * num_2
    print(f'O resultado da operação é {resultado}')
elif oper == '/':
    resultado = num_1 / num_2
    print(f'O resultado da operação é {resultado}')
else:
    print('Digite um operador válido')


if resultado > 0:
    print('O número é positivo')
else:
    print('O número é negativo')


if resultado % 1 == 0:
    print('O número é inteiro')
    if resultado % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
else:
    print('O número é decimal')

