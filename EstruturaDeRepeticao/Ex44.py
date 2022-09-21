from ast import While, match_case


voto = int(input("Digite seu voto \n [1]Manoel \t [2]Elaine \t [3]Jorge \t [4]Creusa \t [5]Nulo \t [6]Voto em Branco"))
votacao = input()

M = voto['1']
E = voto['2'] 
J = voto['3'] 
C = voto['4'] 
N = voto['5'] 
B = voto['6'] 


While (votacao == 's')
    match voto:

        case [1]:
            print("O Número de Votos em Manoel é igual a : ", M)
            M+=M
        case [2] :
            print("O Número de Votos em Elaine é igual a : ", E)
            E+=E
        case [3] :
            print("O Número de Votos em Jorge é igual a : ", J)
            J+=J
        case [4] :
            print("O Número de Votos em Creusa é igual a : ", C)
            C+=C
        case [5] :
            print("O Número de Votos em Nulo é igual a : ", N)
            N+=N
        case [6] :
            print("O Número de Votos em Voto em Branco é igual a : ", B)
            B+=B
    votacao=input("Deseja continuar votando ? \t [s]sim \t [n]não")
    break
    



print("Resultado da Votação")
print("Votos em Manoel = ",M)
print("Votos em Elaine = ",E)
print("Votos em Jorge = ",J)
print("Votos em Creusa = ",C)
print("Votos Nulo = ",N)
print("Votos em Branco = ",B)

