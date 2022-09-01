num1 = float(input("Digite quanto você ganha por horas trabalhadas :"))
num2 = float(input("Quantas horas você trabalha no mês ?"))
R =num1*num2
print("O valor total de seu salário por mês é igual a ",R)



print("A)salário bruto : " ,R)

INSS = (R*8)/100
print (" B)quanto pagou ao INSS : " ,INSS) 

Sindicato = (R*5)/100
print (" C)quanto pagou ao sindicato :",Sindicato)

IR = (R*11)/100
Rliquido = R - Sindicato - INSS - IR
print( " D)o salário líquido : ", Rliquido)

