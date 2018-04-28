#-*- coding: utf-8 -*-
'''
Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50
pessoas. Fazer um algoritmo que calcule e escreva:
- a maior e a menor altura do grupo;
- a média de altura das mulheres;
- o número de homens;
'''

def main():
    maiorAltura = 0.0
    menorAltura = 0.0
    mediaAlturaMulheres = 0.0
    somaAlturaMulheres = 0.0
    contadorMulheres = 0
    contadorHomens = 0

    for laco in range(5):
        print("Pessoa %d:\n" % (laco + 1))
        
        altura = float(input("\tInforme a altura: "))
        #valida altura informado pelo usuário:
        while altura < 0.0:
            print("\n\t[!] Altura invalida [!]")
            altura = input("\tInforme a altura: ")
        
        sexo = input("\tInforme o sexo(F - Feminino ou  M - Masculino): ")
        #valida sexo informado pelo usuário:
        while sexo != 'F' and sexo != 'M' and sexo != 'f' and sexo != 'm':
            print("\n\t[!] Valor de sexo invalido [!]")
            sexo = input("\tInforme o sexo(F - Feminino ou  M - Masculino): ")
        
        if altura < menorAltura or laco == 0:
            menorAltura = altura
        if altura > maiorAltura:
            maiorAltura = altura
        
        if sexo == "F" or sexo == "f":
            somaAlturaMulheres = somaAlturaMulheres + altura
            contadorMulheres = contadorMulheres + 1
        elif sexo == "M" or sexo == "m":
            contadorHomens = contadorHomens + 1
    
    if contadorMulheres > 0:
        mediaAlturaMulheres = somaAlturaMulheres / contadorMulheres

    #resultado:
    print("\n\nRelatório:")
    print("\tMaior altura do grupo: %.2f" % maiorAltura)
    print("\tMenor altura do grupo: %.2f" % menorAltura)
    print("\tMédia de altura das mulheres: %.2f" % mediaAlturaMulheres)
    print("\tNúmero de homens: %d" % contadorHomens)
    print("\n")

    return 0

if __name__ == '__main__':
    main()