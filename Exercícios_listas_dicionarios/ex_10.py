'''10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).'''

temp_medias = []

for i in range(0, 12):
    temp_medias.append(float(input(f'Digite a temperatura média do mês {i+1}: ')))

media_anual = sum(temp_medias)/len(temp_medias)
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

print('Temperaturas foram acima da média em: ')
for i in range(0, 12):
    if temp_medias[i] > media_anual:
        print(meses[i])