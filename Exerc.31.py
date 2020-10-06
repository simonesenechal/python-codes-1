#Exercicios 31

#Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 
# para viagens mais longas.


distance = float(input('Qual a distância da sua viagem? '))
limite = 200
ticket200 = 0.5
ticketup = 0.45

print(' ')

if distance <= limite:
    print(f'O preço da sua passagem é de R${distance * ticket200:.2f}')
else:
    print(f'O preço da sua passagem é de R$ {distance * ticketup:.2f}')




