#Exercicio 10

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 
# Considere US$ 1,00 = R$ 3,27 

mon = float(input('Quanto de dinheiro você tem? R$ '))
dol = 3.27
conv = mon/dol

print(f'R${mon} corresponde a US$ {conv:.2f}, considerando o dólar a US${dol}')



