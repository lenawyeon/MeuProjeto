#Pedra Papel Tesoura. . . 
print("Esse é o jogo pedra papel e tesoura")
print("Jogador 1 digite seu lance:")
JOGADOR_1 = input()
print("Jogador 2 digite seu lance:")
JOGADOR_2 = input()

if JOGADOR_1 == JOGADOR_2:
    print("Empatados, tentem novamente!")
elif JOGADOR_1 == "pedra" and JOGADOR_2 == "papel":
    print("Jogador 2 você venceu!")
elif JOGADOR_1 == "pedra" and JOGADOR_2 == "tesoura":
    print("Jogador 1 você venceu!")
elif JOGADOR_1 == "papel" and JOGADOR_2 == "pedra":
    print("Jogador 1 você venceu!")
elif JOGADOR_1 == "papel" and JOGADOR_2 == "tesoura":
    print("Jogador 2 você venceu!")
elif JOGADOR_1 == "tesoura" and JOGADOR_2 == "pedra":
    print("Jogador 2 você venceu!")
elif JOGADOR_1 == "tesoura" and JOGADOR_2 == "papel":
    print("Jogador 1 você venceu!")
elif JOGADOR_2 == "pedra" and JOGADOR_1 == "papel":
    print("Jogador 2 você venceu!")
elif JOGADOR_2 == "pedra" and JOGADOR_1 == "tesoura":
    print("Jogador 1 você venceu!")
elif JOGADOR_2 == "papel" and JOGADOR_1 == "pedra":
    print("Jogador 1 você venceu!")
elif JOGADOR_2 == "papel" and JOGADOR_1 == "tesoura":
    print("Jogador 2 você venceu!")
elif JOGADOR_2 == "tesoura" and JOGADOR_1 == "pedra":
    print("Jogador 2 você venceu!")
elif JOGADOR_2 == "tesoura" and JOGADOR_1 == "papel":
    print("Jogador 1 você venceu!")
