#Time de futebol. . . 
print("Qual a sua posição no jogo de futebol; goleiro, zagueiro, lateral, ala, volante, meia, ponta, atacante ou centroavante?")
POSIÇÃO = input()

if POSIÇÃO == "goleiro" or POSIÇÃO == "zagueiro" or POSIÇÃO == "lateral":
    print("Você é da defesa!")
elif POSIÇÃO == "ala" or POSIÇÃO == "volante" or POSIÇÃO == "meia":
    print("Você é do meio-campo!")
elif POSIÇÃO == "ponta" or POSIÇÃO == "atacante" or POSIÇÃO == "centroavante":
    print("Você é do ataque!")
else:
    print("Teimoso!")