#-*- coding: utf-8 -*-
'''
Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário para
que essa massa se torne menor do que 0,5 grama. Escreva a massa inicial, a massa final e o
tempo calculado em horas, minutos e segundos.

'''
def main():
    massaInicial = float(input("Informe a massa inicial (gramas): "))
    massaFinal = massaInicial
    tempo = 0
    
    while(massaFinal >= 0.5):
        massaFinal = massaFinal / 2.0
        tempo += 50
    
    horas = tempo // 3600
    tempoRestante = tempo % 3600    
    minutos = tempoRestante // 60
    segundos = tempoRestante % 60
    
    print("\nRelatório:")
    print("\tMassa inicial: \t%.6fg" % massaInicial)
    print("\tMassa final: \t%.6fg" % massaFinal)
    print("\tTempo: \t\t%d:%d:%d" % (horas, minutos, segundos))
    print()

    return 0

if __name__ == '__main__':
    main()