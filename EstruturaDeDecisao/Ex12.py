SALHR = hr = Sal = INSS = IR = Des = Salliq = FGTS = 0


print("Folha de Pagamento \n")
salhr =  float(input("Digite o valor do seu salário por hora no mês  :"))
hr = float(input("Digite a quantidade de horas trabalhadas no mês"))



Sal = (salhr * hr)
INSS =(Sal*10)/100
IR = (Sal*5)/100
Des = IR + INSS
Salliq = Sal - Des
FGTS = (11*Sal)/100

if (Sal <= 900):
    print("Isento")
    Des = 0
    print(Salliq)
elif((Sal>900)and(Sal<=1500)):
    print("Desconto de 5%")
    print((Sal*5)/100)
    print(Salliq -(Sal*5)/100)
elif((Sal>1500)and(Sal<=2500)):
    print("Desconto de 10%")
    print((Sal*10)/100)
    print(Salliq-(Sal*10)/100)
else:
    print("Desconto de 20%")    
    print("Salário Bruto:      : ",Sal)
    print("(-) IR (5%)                     : ",IR)
    print("(-) INSS ( 10%)                 : ",INSS)	
    print("FGTS (11%)                      : ",FGTS)
    print("Total de descontos              : ",Des)
    print("Salário Liquido                 : ",Salliq)
    print((Sal*20)/100)


   




