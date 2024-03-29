'''11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
• Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
• Triângulo Equilátero: três lados iguais;
• Triângulo Isósceles: quaisquer dois lados iguais;
• Triângulo Escaleno: três lados diferentes.'''

lado_1 = int(input('Digite o tamanho do 1º lado: '))
lado_2 = int(input('Digite o tamanho do 2º lado: '))
lado_3 = int(input('Digite o tamanho do 3º lado: '))

if ((lado_1 + lado_2) > lado_3) and ((lado_1 + lado_3) > lado_2) and ((lado_2 + lado_3) > lado_1):
    if lado_1 == lado_2 == lado_3:
        print('Medidas de um triângulo Equilátero.')
    elif lado_1 != lado_2 != lado_3:
        print('Medidas de um triângulo Escaleno.')
    else:
        print('Medidas de um triângulo Isósceles.')
else:
    print('Não podemos criar um triângulo com essas medidas.')
