# agora vou entrar os dados do usuario

nome = input("DIGITE SEU NOME: ")
idade = input("DIGITE SUA IDADE: ")
altura = float(input("Digite Sua altura: "))
peso = float(input("Digite seu Peso"))
imc = peso/altura**2

print("-"*30)
print("DADOS DO PACIENTE:")
print("NOME: ", nome)
print("IDADE: ", idade, " Anos")
print("SEU IMC: ", imc)

