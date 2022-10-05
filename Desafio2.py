refeicao = -1
calorias = 0
calFinal = 0

print ("\n######## Este é um desafio proposto pela faculdade FIAP no Curso de Banco de Dados ########")
print("############### Este é um programa que calcula quantas calorias você ingeriu no dia ###############")

while refeicao != 0:

    print("\nEscolha uma das refeições abaixo e insira a quantidade de calorias que ingeriu:")
    print("\n1 - Café da manhã" + "\n2 - Lanche da Manhã" + "\n3 - Almoço" + "\n4 - Lanche da tarde" + "\n5 - Jantar" + "\n6 - Ceia" + "\n0 - FINALIZAR \n")

    refeicao = int(input("Digite a refeição: "))

    if refeicao not in (1,2,3,4,5,6,0):
        calorias = calFinal
        print("\nOPÇÃO INVÁLIDA!!!")


    elif refeicao in (1,2,3,4,5,6):
        calorias = int(input("\nDigite a quantidade de calorias dessa refeição: "))
        calFinal += calorias

    elif refeicao == 0:
        print("\nVocê ingeriu {} kcal hoje".format(calFinal))
