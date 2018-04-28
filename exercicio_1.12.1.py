#-*- coding: utf-8 -*-
'''
Fazer um algoritmo que:
- Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A
última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e
escreva a idade média deste grupo de indivíduos.
'''

def main():
    
    age = 0; sum = 0; count = 0
    media = 0.0

    while True:
        age = int(input("informe uma idade: "))
        sum = sum + age
        if age == 0:
            break
        count = count + 1

    media = sum / count
    print("\nMedia da idades informadas é %2.f\n" % media)
    
    return 0

if __name__ == '__main__':
	main()