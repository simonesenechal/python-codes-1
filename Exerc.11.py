#Exercicio 11

#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área 
#e a quantidade de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m² 

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
pintura = area / 2

print(f'A altura da parede é de {altura}m, a largura {largura}m, sendo o total \
da area de {area:.2f}m neste caso são necessárias {pintura:.2f} litros de tinta para a pintura')


