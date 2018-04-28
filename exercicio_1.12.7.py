#-*- coding: utf-8 -*-
'''
Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova
de Programação de Computadores para cada uma das 14 turmas existentes. Para cada turma,
é fornecido um conjunto de valores, sendo que os dois primeiros valores do conjunto
corresponde a identificação da turma (A, ou B, ou C,...) e ao número de alunos matriculados, e
os demais valores deste conjunto contêm o número de matrícula do aluno e a letra A ou P para
o caso de o aluno estar ausente ou presente, respectivamente. Fazer um algoritmo que:
- para cada turma, calcule a porcentagem de ausência e escreva a identificação da
turma e a porcentagem calculada;
- determine e escreva quantas turmas tiveram porcentagem de ausência superior a 5%.

'''
def main():
    contadorPercentualAusenciaAcima5 = 0

    for turma in range(14):
        print("---------------------------------------------------------------------------------------")
        contadorAusenciaTurma = 0

        identificacao = input("Informe a identificação da turma: ")        
        numeroAlunos = int(input("Informe o número de alunos matriculados: "))
        
        print("\nTurma [%d - %s] - Alunos:" % (turma, identificacao))
        for aluno in range(numeroAlunos):
            print("\nAluno %d:" % (aluno + 1))
            matricula = input("\t\tInforme a matricula: ")            
            situacao = input("\t\tInforme a situação (A - Ausente ou  P - Presente): ")
            
            #validação da situação informada:
            while(situacao != 'A' and situacao != 'P' and situacao != 'a' and situacao != 'p'):
                print("\t\t[!]Situação invalida[!]")
                situacao = input("\t\tInforme a situação (A - Ausente ou  P - Presente): ")
            
            if situacao == 'A' or situacao == 'a':
                contadorAusenciaTurma += 1
        
        if numeroAlunos > 0:
            percentualAusencias = (contadorAusenciaTurma * 100)/numeroAlunos

        if percentualAusencias > 5:
            contadorPercentualAusenciaAcima5 += 1

        print("\nTurma [%s]: %.2f%% de alunos ausentes" % (identificacao, percentualAusencias))
    print("---------------------------------------------------------------------------------------")
    print("\nQuantidade de turmas com ausencias acimas de 5%%: %d" % contadorPercentualAusenciaAcima5)
    print()

    return 0

if __name__ == '__main__':
    main()