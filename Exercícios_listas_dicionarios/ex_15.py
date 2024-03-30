'''15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.'''

idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

media_setor = 0
qtd_acima_media = 0
total_idades = 0

for setor, idade in idades.items():
    media_setor = sum(idade)/len(idade)
    print(f'Média de idade do {setor}: {media_setor}')
    total_idades += sum(idade)
media_total = total_idades / (len(idade)*len(idades))
print(f'A média de idade geral é {media_total}')

for setor, idade in idades.items():
    for id in idade:
        if id > media_total:
            qtd_acima_media += 1
print(f'{qtd_acima_media} pessoas estão acima da idade média geral')