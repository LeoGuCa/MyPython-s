medImpar = 0.0
medPar = 0.0

print ("\n######## Este é um desafio proposto pela faculdade FIAP no Curso de Banco de Dados ########")
print ("\n######## Esse programa calcula a nota dos alunos impares, depois dos alunos pares. A Média de cada tipo de aluno será exibida no final ########")

for x in range(1, 50, 2):
        print("\n######## VOCÊ ESTÁ DIGITANDO AS NOTAS DO ALUNOS ÍMPARES ########")
        ntImpar = float(input("\nPor favor, digite a nota do aluno de número {}: ".format(x)))

        medImpar += ntImpar

medImpar = medImpar / 5

for x in range(2, 51, 2):
        print ("\n######## VOCÊ ESTÁ DIGITANDO AS NOTAS DO ALUNOS PARES ########")
        ntPar = float(input("\nPor favor, digite a nota do aluno de número {}: ".format(x)))

        medPar += ntPar

medPar = medPar / 5

print("A média dos alunos ímpares foi de {}".format(medImpar))
print("A média dos alunos pares foi de {}".format(medPar))