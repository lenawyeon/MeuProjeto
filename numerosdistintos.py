#Ordem crescente ou decrescente. . .
X = int(input("Digite um número:"))
Y = int(input("Digite um número:"))
Z = int(input("Digite um número:"))

if X > Y > Z:
    print("Os números estão em ordem decrescente")
elif X < Y < Z:
    print("Os números estão em ordem crescente")
else:
    print("Os números estão misturados")