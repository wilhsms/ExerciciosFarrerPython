#-*- coding: utf-8 -*-
'''
Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa
cidade, num determinado dia. Para cada casa visitada, é fornecido o número do canal
(4,5,7,12) e o número de pessoas que o estavam assistindo naquela casa. Se a televisão
estivesse desligada, nada era anotado, ou seja, esta casa não entrava na pesquisa. Fazer um
algoritmo que:
- leia um número indeterminado de dados, sendo que o “FLAG” corresponde ao número do
canal igual a zero;
- calcule a porcentagem de audiência para cada emissora;
- escreva o número do canal e a sua respectiva porcentagem.

'''
def main():
    numeroCanal = 1; numeroPessoasAssistindoCasa = 0; contadorTotalPessoas = 0
    
    contadorPessoasCanal04 = 0; contadorPessoasCanal05 = 0
    contadorPessoasCanal07 = 0; contadorPessoasCanal12 = 0
    
    percentualAudienciaCanal04 = 0.0; percentualAudienciaCanal05 = 0.0
    percentualAudienciaCanal07 = 0.0; percentualAudienciaCanal12 = 0.0
       
    while numeroCanal != 0:
        numeroCanal = int(input("Informe o canal assitido: "))
        #validação do numero canal:
        while numeroCanal != 0 and numeroCanal != 4 and numeroCanal != 5 and numeroCanal != 7 and numeroCanal != 12:
            print("\tNúmero de canal invalido!")
            numeroCanal = int(input("Informe o canal assitido: "))
        
        if numeroCanal != 0:
            numeroPessoasAssistindoCasa = int(input("Informe a quantidade de pessoas assintindo TV: "))
            contadorTotalPessoas += numeroPessoasAssistindoCasa

            if numeroCanal == 4:
                contadorPessoasCanal04 += numeroPessoasAssistindoCasa
            elif numeroCanal == 5:
                contadorPessoasCanal05 += numeroPessoasAssistindoCasa
            elif numeroCanal == 7:
                contadorPessoasCanal07 += numeroPessoasAssistindoCasa
            elif numeroCanal == 12:
                contadorPessoasCanal12 += numeroPessoasAssistindoCasa
       
    if contadorTotalPessoas > 0.0:
        percentualAudienciaCanal04 = (contadorPessoasCanal04 * 100) / contadorTotalPessoas
        percentualAudienciaCanal05 = (contadorPessoasCanal05 * 100) / contadorTotalPessoas
        percentualAudienciaCanal07 = (contadorPessoasCanal07 * 100) / contadorTotalPessoas
        percentualAudienciaCanal12 = (contadorPessoasCanal12 * 100) / contadorTotalPessoas

    print("\nRelatório de Audências: ")
    print("\tCanal 04:\t%.2f %%" % percentualAudienciaCanal04)
    print("\tCanal 05:\t%.2f %%" % percentualAudienciaCanal05)
    print("\tCanal 07:\t%.2f %%" % percentualAudienciaCanal07)
    print("\tCanal 12:\t%.2f %%" % percentualAudienciaCanal12)
    print()
            
    return 0

if __name__ == '__main__':
    main()