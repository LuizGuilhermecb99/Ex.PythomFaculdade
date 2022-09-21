num1 = float(input("Qual a quantidade em metros a ser pintada ? "))

Quantidade = num1/6
Preco1 = Quantidade*(80/18)
Preco2=Quantidade*(25/3,6)
Latas = num1/54
Latas2 = num1/10,8


X = input(print("Qual tipo de serviço o senhor vai usar ? \n A)Apenas Latas grandes \n B)Apenas Latas Pequenas \n C)Ambas"))

if (X == "A"):
    print("A Quantidade de latas q serem usadas é igual a : ",Latas)
    print ("O Preço a ser pago é igual a : ",Preco1, " Reais")
elif (X == "B"):
    print("A Quantidade de latas q serem usadas é igual a : ",Latas2)
    print ("O Preço a ser pago é igual a : ",Preco2, " Reais")
else:
    print("")

