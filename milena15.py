#Programa 1 de tv/série. . .
print(input("Digite um filme ou série de sua preferência:"))
print("Qual nota vc da pra esse programa de 1 a 5?")
print("1")
print("2")
print("3")
print("4")
print("5")
NOTA = int(input())

match NOTA:
    case 1:
        print("Péssimo")
        PORQUE = input("Porque seu programa recebeu essa nota?")
    case 2:
        print("Ruim")
        PORQUE = input("Porque seu programa recebeu essa nota?")
    case 3:
        print("Razoável")
    case 4:
        print("Bom")
    case 5:
        print("Excelente")
    case _:
        print("ALERTA")
