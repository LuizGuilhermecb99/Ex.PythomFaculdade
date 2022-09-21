num1 = input("Digite o tamanho de um arquivo para download (em MB) ")
num2 = input("Digite a velocidade de um link de Internet (em Mbps) ")
R = (num1/(num2/8))

print ("o tempo aproximado de download do arquivo usando este link (em minutos) é igual a : ",R/60)