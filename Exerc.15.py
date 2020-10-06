#Exercicio 15

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado. 



days = float(input('Quantidade de dias do aluguel do carro: '))
km = float(input('Qual km percorrida: '))
rent = (days * 60) + (km * 0.15)

print(f'O preço total do aluguel do carro a ser pago é de R${rent}.')


