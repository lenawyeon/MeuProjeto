#Programa 1. . .
X = float(input("Digite um número:"))
Y = float(input("Digite outro número:"))
Z = float(input("Digite mais um número:"))
W = float(input("Digite um quarto número:"))

MÉDIA = (X + Y + Z + W) / 4

print("Essa é sua média:", MÉDIA)

if MÉDIA < 6:
    print("Você está REPROVADO")
else:
    print("Você está APROVADO")


#Programa 2. . .
X = float(input("Digite seu peso:"))
Y = float(input("Digite sua altura:"))

IMC = X / Y
print("Seu IMC é:", IMC)

if IMC > 25:
    print("Acima do peso ideal")
elif IMC < 18:
    print("Abaixo do peso ideal")
elif 18 < IMC < 25:
    print("Seu peso está OK!")


