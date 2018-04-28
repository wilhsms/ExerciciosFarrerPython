#-*- coding: utf-8 -*-
'''
A conversão de graus Farenheit para centígrados é obtida por C = (5 x (F - 32))/9
Fazer um algoritmo que calcule e escreva uma tabela de centígrados em função de graus
Farenheit, que variam de 50 a 150 de 1 em 1.

'''
def main():
    print("Fahrenheit \t Celsius")
    for fahrenheit in range(50, 151):
        celsius = (5.0 * (fahrenheit - 32))/ 9.0
        print("%.2fº \t\t %.2fº" % (fahrenheit, celsius))
    
    return 0

if __name__ == '__main__':
    main()