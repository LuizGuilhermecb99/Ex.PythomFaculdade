from ast import While, match_case

votacao = 0

while votacao == 0:

    voto = int(input("Digite seu voto \n [1]Manoel \t [2]Elaine \t [3]Jorge \t [4]Creusa \t [5]Nulo \t [6]Voto em Branco \n"))
    votacao = input("Digite [0] para começar e [7] para terminar")
    
    M = voto[1]
    E = voto[2] 
    J = voto[3] 
    C = voto[4] 
    N = voto[5] 
    B = voto[6] 

    T = M + E + J + C + N + B # Voto total

    PN = N/T # Porcentagem de votos nulos/total

    PB = B/T # Porcentagem de votos brancos/total

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
         


    
print("Fim de Votação \n")
    

print("Resultado da Votação \n")
print("Votos em Manoel = ",M)
print("Votos em Elaine = ",E)
print("Votos em Jorge = ",J)
print("Votos em Creusa = ",C)
print("----------------------")
print("Votos Nulo = ",N)
print("Votos em Branco = ",B)
print("porcentagem votos nulos/total = ",PN)
print("porcentagem votos brancos/total = ",PB)

