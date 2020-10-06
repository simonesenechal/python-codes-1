#Exercicio 29

#Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80 km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$ 7,00 por cada Km acima do limite. 

velocidade = float(input('Qual a velocidade do carro? '))
limite = 80
multa = 7

print(' ')

print(f'O limite de velocidade é de 80km/h e a sua velocidade é de {velocidade}')

print(' ')
if velocidade < limite:
    print(f'Você está dentro do limite de velocidade.')
else:
    print(f'Você ultrapassou o limite de velocidade, sua multa é no valor de \
    R${(velocidade-limite)*multa:.2f}.')



