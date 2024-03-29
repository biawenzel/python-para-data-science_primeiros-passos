'''9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
- Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
- Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.'''

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulos = 0
brancos = 0

for i in range(1, 21):
    voto = input('Digite seu voto (candidatos - 1, 2, 3 ou 4 / nulo - 5 / em branco - 6): ')
    if voto == '1':
        candidato_1 += 1
    elif voto == '2':
        candidato_2 += 1
    elif voto == '3':
        candidato_3 += 1
    elif voto == '4':
        candidato_4 += 1
    elif voto == '5':
        nulos += 1
    elif voto == '6':
        brancos += 1
    else:
        print('Voto inválido.')
    i += 1
porc_nulos = (nulos/20)*100
porc_brancos = (brancos/20)*100

print(f'Candidato 1: {candidato_1} votos \nCandidato 2: {candidato_2} votos \nCandidato 3: {candidato_3} votos \nCandidato 4: {candidato_4} votos \nVotos nulos: {nulos} votos ({porc_nulos}%) \nVotos em branco: {brancos} votos ({porc_brancos}%)')
