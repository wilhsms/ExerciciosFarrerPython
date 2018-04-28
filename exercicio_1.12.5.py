#-*- coding: utf-8 -*-
'''
Supondo que a população de um país A seja da ordem de 90.000.000 de habitantes
com uma taxa anual de crescimento de 3% e que a população de um país B seja,
aproximadamente, de 20.000.000 de habitantes com uma taxa anual de crescimento de 1,5%,
fazer um algoritmo que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento.

'''
def main():
    anos = 0
    habitantesPaisA = 90000000
    habitantesPaisB = 200000000

    while(habitantesPaisA < habitantesPaisB):
        habitantesPaisA = habitantesPaisA * 1.03
        habitantesPaisB = habitantesPaisB * 1.015
        anos += 1

    mensagem = "São necessários {0:,} anos para que o pais A ultrapasse o pais B".format(anos).replace(',', '.')
    print(mensagem)

    return 0

if __name__ == '__main__':
    main()