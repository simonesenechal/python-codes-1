#Exercicios 12

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto 

price = float(input('Qual o preço do produto? '))
discount = price * 0.05
newprice = price - discount

print(f'O valor do produto é R${price:.2f} menos o desconto de 5% fica por R${newprice:.2f}.')





