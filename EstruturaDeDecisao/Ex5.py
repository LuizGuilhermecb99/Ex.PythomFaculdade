#Lista de Exercícios : Estrutura de Decisão.

num1 = float(input("Qual a primeira nota ? "))
num2 = float(input("Qual a segunda nota ? "))

R = (num1 + num2)/2

if ((R >= 7.0 ) and (R  <10.0)):
    print("Aluno Aprovado !!")
elif(R == 10.0):
    print("Aluno Aprovado com Distinção !!")
else:
    print("Aluno Reprovado !!")



