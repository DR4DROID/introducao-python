alcool = float(input("Digite o valor do alcool: "))
gasolina = float(input("Digite o valor do gasolina: "))
resultado = alcool/gasolina

if resultado < 0.70:
    print ("ABASTEÇA COM ALCOOL")
else:
    print ("ABASTEÇA COM GASOLINA")