'''2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.'''

col_a = 4
col_b = 10
dias = 0

while col_a <= col_b:
    col_a = col_a + (col_a * 0.03)
    col_b = col_b + (col_b * 0.015)
    dias += 1
print(f'A colônia A ultrapassou a B em {dias} dias.')