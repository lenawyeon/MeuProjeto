#Avaliação de serviços. . . 
print("Você prestou algum serviço?")
RESPOSTA = input()

if RESPOSTA == "SIM":
    print("De uma nota de 1 a 5:")
    NOTA = int(input())
    if NOTA == 1:
        print("péssimo")
    elif NOTA == 2:
        print("ruim")
    elif NOTA == 3:
        print("razoável")
    elif NOTA == 4:
        print("bom")
    elif NOTA == 5:
        print("ótimo")
elif RESPOSTA == "NÃO":
    print("0")
