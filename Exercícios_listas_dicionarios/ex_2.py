'''2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.'''

gastos_empresa = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

acima_3000 = 0
for gasto in gastos_empresa:
    if gasto > 3000:
        acima_3000 += 1

qtd_compras = len(gastos_empresa)
porcentagem_acima_3000 = (acima_3000/qtd_compras) * 100

print(f'{acima_3000} compras acima de R$3000.00, que representam {porcentagem_acima_3000}% das compras')
