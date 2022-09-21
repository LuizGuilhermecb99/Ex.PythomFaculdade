print("O Preço do peixe é de 32 reais por quilogrmaa(kilo)")
Pesopeixe = int(input("Insira  o Peso do peixe em quilogramas(Kg)"))

Precopeixe = 32*Pesopeixe

excesso = Pesopeixe - 50

if(Pesopeixe > 50):
    Precopeixe += Pesopeixe*4
    multa = Precopeixe - (excesso*4)
else:
    multa = 0
    Precopeixe = 32*Pesopeixe
    


print("O Valor do peixe a ser pago é igual a :",Precopeixe, "\n O Valor da Multa é igual a : ",multa)
print("O Valor do execsso de peso é igual a : ", excesso)