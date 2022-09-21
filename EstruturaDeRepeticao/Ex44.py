from ast import While, match_case

votacao = T = M = E =J = C = N = B = 0

print('\n-------------------Eleições 2022-------------------------\n')

print("\t \t \t Candidatos ! \n [1]Manoel \t [2]Elaine \t [3]Jorge \t [4]Creusa \t [5]Nulo \t [6]Voto em Branco \n")

votacao = int(input("Deseja realizar a votação ? [1] sim \t [0] não \n"))

while votacao != 0:

    voto = int(input(" Digite o número do seu candidato: \n "))
        
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
    T = T +1
    votacao = int(input("Deseja continuar votando ? \t [1] sim \t [0] não \n"))
         

PN = N/T # Porcentagem de votos nulos/total

PB = B/T # Porcentagem de votos brancos/total

print("Fim de Votação \n")
print("Resultado da Votação \n")
print("Total de Votos = ",T)
print("Votos em Manoel = ",M)
print("Votos em Elaine = ",E)
print("Votos em Jorge = ",J)
print("Votos em Creusa = ",C)
print("----------------------")
print("Votos Nulo = ",N)
print("Votos em Branco = ",B)
print("porcentagem votos nulos/total = ",PN, "%")
print("porcentagem votos brancos/total = ",PB ,"%")

