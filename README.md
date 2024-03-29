# Python para Data Science - primeiros passos

## Exercícios - Estruturas condicionais

1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

6) Escreva um programa que leia três números e os exiba em ordem decrescente.

7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes.

12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
- O valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
- O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
- Para variação acima de 20%: bonificação para o time de vendas.
- Para variação entre 2% e 20%: pequena bonificação para time de vendas.
- Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
- Para bonificações abaixo de -10%: corte de gastos.

## Exercícios - Estruturas de repetição

1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

_Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20_

7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
- Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
- Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.