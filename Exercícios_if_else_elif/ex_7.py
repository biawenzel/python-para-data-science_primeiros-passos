'''7)Escreva um programa que pergunte em qual turno a pessoa usuária estuda 
("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", 
ou "Valor Inválido!", conforme o caso.'''
turno = input('Em qual turno você estuda? ') 

if (turno == 'manhã') or (turno == 'Manhã'):
    print('Bom dia!')
elif (turno == 'tarde') or (turno == 'Tarde'):
    print('Boa tarde!')
elif (turno == 'noite') or (turno == 'Noite'):
    print('Boa noite!')
else:
    print('Valor inválido.')