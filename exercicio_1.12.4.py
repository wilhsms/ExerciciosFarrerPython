#-*- coding: utf-8 -*-
'''
Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele
comercializa. Para isto, mandou digitar uma linha para cada mercadoria com nome, preço de
compra e preço de venda das mesmas. Fazer um algoritmo que:determine e escreva quantas
mercadorias proporcionam:
    lucro < 10%
    10% <= lucro <= 20%
    lucro > 20%
determine e escreva o valor total de compra e de venda de todas as mercadorias, assim como
o lucro total.
Observação: o aluno deve adotar um flag.

'''
def main():
    contadorLucroMenor10 = 0
    contadorLucroEntre10_20 = 0
    contadorLucroMaior20 = 0
    somaPrecoVenda = 0.0
    somaPrecoCompra = 0.0
    somaLucro = 0.0
    
    contadorProduto = 1

    while True:
        print("Produto %d:" % contadorProduto)
        
        nome = input("\tInforme o nome (ou apenas Enter para sair): ")
        if not nome:
            print("\t[Saiu]")
            break
        
        valor = input("\tInforme o preço de compra (ou apenas Enter para sair): ")
        if not valor:
            print("\t[Saiu]")
            break
        precoCompra = float(valor)

        valor = input("\tInforme o preço de venda (ou apenas Enter para sair): ")
        if not valor:
            print("\t[Saiu]")
            break
        precoVenda = float(valor)

        lucro = precoVenda - precoCompra
        lucroPercentual = lucro/precoVenda * 100

        if lucroPercentual < 10:
            contadorLucroMenor10 += 1
        elif lucroPercentual >= 10 and lucroPercentual <= 20:
            contadorLucroEntre10_20 += 1
        elif lucroPercentual > 20:
            contadorLucroMaior20 += 1

        somaPrecoCompra += precoCompra
        somaPrecoVenda += precoVenda
        somaLucro += lucro

        contadorProduto += 1

    print("\n\nRelatório:")
    print("\tQuantidade de produtos com lucro menor que 10%%: \t%d item(s)" % contadorLucroMenor10)
    print("\tQuantidade de produtos com lucro entre 10%% e 20%%: \t%d item(s)" % contadorLucroEntre10_20)
    print("\tQuantidade de produtos com lucro acima de 20%%: \t\t%d item(s)" % contadorLucroMaior20)
    print("\tValor total de compra de todos os produtos: \t\tR$ %.2f" % somaPrecoCompra)
    print("\tValor total de venda de todos os produtos: \t\tR$ %.2f" % somaPrecoVenda)
    print("\tValor total de lucro de todos os produtos: \t\tR$ %.2f" % somaLucro)
    print()

    return 0

if __name__ == '__main__':
    main()