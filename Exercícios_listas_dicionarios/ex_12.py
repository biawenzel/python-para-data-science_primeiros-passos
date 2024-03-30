'''12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.'''

votos = {'Design 1':1334, 'Design 2':982, 'Design 3':1751, 'Design 4':210, 'Design 5':1811}
vencedor = ''
qtd_votos_vencedor = 0

for i in votos.keys():
    if votos[i] > qtd_votos_vencedor:
        qtd_votos_vencedor = votos[i]
        vencedor = i
print(f'O design vencedor é o {vencedor} com {qtd_votos_vencedor} votos')