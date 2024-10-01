#gabarito. . . 

GABARITO = ["B", "C", "A", "E", "D"]
RESPOSTAS = ["", "", "", "", ""]
ACERTOS = 0

for X in range(len(GABARITO())):
    print(f"Digite a resposta {X+1}:")
    RESPOSTAS[X] = input()
    if GABARITO == RESPOSTAS[X]:
        print("Acertou!")
        ACERTOS = ACERTOS + 1
    else:
        print("Errou!")

print("Total de acertos:", ACERTOS)
 