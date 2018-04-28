#-*- coding: utf-8 -*-
'''
Uma certa firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou
não de um novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado e sua
resposta (sim ou não). Sabendo-se que foram entrevistadas 2.000 pessoas, fazer um algoritmo
que calcule e escreva:
- o número de pessoas que responderam sim;
- o número de pessoas que responderam não;
- a porcentagem de pessoas do sexo feminino que responderam sim;
- a porcentagem de pessoas do sexo masculino que responderam não;

'''
def main():
    sexo = ''; resposta = ''
    contadorSim = 0; contadorNao = 0; contadorFemininoSim = 0; contadorMasculinoNao = 0
    percentualFemininoSim = 0.0; percentualMasculinoNao = 0.0

    for pessoa in range(2000):
        print("---------------------------------------------------------------------------------------")
        print("Entrevistado [%d]" % (pessoa + 1))
        
        sexo = input("\tInforme o sexo (M - Masculino ou  F - Feminino): ")
        while sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo != 'f':
            print("\t\t[!]Sexo invalido[!]")
            sexo = input("\tInforme a sexo (M - Masculino ou  F - Feminino): ")

        resposta = input("\tInforme a resposta (S - Sim ou  N - Não): ")
        while resposta != 'S' and resposta != 'N' and resposta != 's' and resposta != 'n' :
            print("\t\t[!]Resposta invalida[!]")
            resposta = input("\tInforme a resposta (S - Sim ou  N - Não): ")
        
        if resposta == 'S' or resposta == 's':
            contadorSim += 1
            if sexo == 'F' or sexo == 'f' :
                contadorFemininoSim += 1
        else:
            contadorNao += 1
            if sexo == 'M' or sexo == 'm' :
                contadorMasculinoNao += 1
        
    percentualFemininoSim = (contadorFemininoSim * 100) / (contadorSim + contadorNao)
    percentualMasculinoNao = (contadorMasculinoNao * 100) / (contadorSim + contadorNao)

    print("\nRelatório:")
    print("\tNúmero de pessoas que responderam sim: \t\t%d" % contadorSim)
    print("\tNúmero de pessoas que responderam não: \t\t%d" % contadorNao)
    print("\tPercentual de pessoas do sexo feminino que responderam sim: \t%.2f %%" % percentualFemininoSim)
    print("\tPercentual de pessoas do sexo masculino que responderam nao: \t%.2f %%" % percentualMasculinoNao)
    print()
    
    return 0

if __name__ == '__main__':
    main()