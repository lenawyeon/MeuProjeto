#Lista de afazeres. . .
print("Meus afazeres:")
AFAZERES = ["1.Meditar", "2.Academia", "3.Estudar", "4.Levar cachorro pra passear", "5.Trabalhar"]
RESPOSTA = 0

for X in AFAZERES:
    print(X)

for X in range(len(AFAZERES)):
    print(f"A tarefa {X+1} já foi feita?")
    RESPOSTA = input()
    if RESPOSTA == "sim":
        del(AFAZERES[X])
        print("Tarefa excluida, pois já foi feita!")
    else:
        print()

print("Quer add uma nova tarefa?")
RESPOSTA = input()
if RESPOSTA == "sim":
 AFAZERES.append()
 




