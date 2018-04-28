#-*- coding: utf-8 -*-
'''
Foi feita uma pesquisa para determinar o índice de mortalidade infantil em um certo
período. Fazer um algoritmo que:
- leia inicialmente o número de crianças nascidas no período;
- leia, em seguida um número indeterminado de linhas, contendo, cada uma, o sexo de uma
criança morta (masculino, feminino) e o número de meses de vida da criança. A última linha,
que não entrará nos cálculos, contém no lugar do sexo a palavra “vazio”;
- determine e imprima:
a) a porcentagem de crianças mortas no período;
b) a porcentagem de crianças do sexo masculino mortas no período;
c) a porcentagem de crianças que viveram 24 meses ou menos no período.
'''
def main():
    numeroCriancasNascidas = 0
    sexo = ''; numeroMesesDeVida = 0
    contadorCriancasMortas = 0; contadorCriancasMortasMasculino = 0; contadorCriancasMortasViveram24Meses = 0
    percentualCriancasMortas = 0.0; percentualCriancasMortasMasculino = 0.0; percentualCriancasMortasViveram24Meses = 0.0

    numeroCriancasNascidas = int(input("Informe o número de crianças nascidas no periodo: "))

    while sexo != 'vazio':
        print("------------------------------------------------")
        print("Criança Morta [%d]" % (contadorCriancasMortas + 1))
        sexo = input("\tInforme o sexo (M - Masculino ou  F - Feminino), ou a palavra ""vazio"" para sair: ")
        while sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo != 'f' and sexo != 'vazio':
            print("\t\t[!]Sexo invalido[!]")
            sexo = input("\tInforme a sexo (M - Masculino ou  F - Feminino), ou a palavra vazio para sair: ")
        
        #condição de saida:
        if sexo == 'vazio': 
            break
        
        numeroMesesDeVida = int(input("\tInforme o número de meses de vida: "))
        if sexo == 'M' or sexo == 'm':
            contadorCriancasMortasMasculino += 1
        
        if numeroMesesDeVida <= 24:
            contadorCriancasMortasViveram24Meses += 1

        contadorCriancasMortas += 1
    
    percentualCriancasMortas = (contadorCriancasMortas * 100) / numeroCriancasNascidas
    percentualCriancasMortasMasculino = (contadorCriancasMortasMasculino * 100) / numeroCriancasNascidas
    percentualCriancasMortasViveram24Meses = (contadorCriancasMortasViveram24Meses * 100) / numeroCriancasNascidas

    print("\nRelatório:")
    print("\tPercentual de crianças mortas no período: \t\t\t%.2f %%" % percentualCriancasMortas)
    print("\tPercentual de crianças do sexo masculino mortas no período: \t%.2f %%" % percentualCriancasMortasMasculino)
    print("\tPercentual de crianças que viveram por até 24 meses: \t\t%.2f %%" % percentualCriancasMortasViveram24Meses)    
    print()
    
    return 0

if __name__ == '__main__':
    main()