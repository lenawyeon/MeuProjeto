#Demonstrações do or/and/not. . .
print("O que você vai fazer amanhã de manhã?")
print("Dormir / Estudar / Planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("Treinar / estudar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você precisa dizer o que vai fazer")
else:
    if MANHA == "dormir" or TARDE == "jogar":
        print("Você está disperdiçando seu dia")
    elif MANHA == "estudar" or TARDE == "treinar":
        print("Que bom! Você irá se aperfeiçoar")
    elif MANHA == "planejar" and TARDE == "trabalhar":
        print("Para trabalhar melhor preciso planejar")
    else:
        print("Não combinamos essas ações. . .")

print("tenha um bom dia!")