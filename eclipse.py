#Possibilidade de ver un eclipse. . . 
print("Em qual estado do sudoeste você está?")
ESTADO = input()
print("Quais as condições; dia claro ou dia escuro?")
CONDIÇÕES = input()
print("Qual horário?")
HORÁRIO = input()

if ESTADO == "RIO DE JANEIRO" and CONDIÇÕES == "dia claro" and HORÁRIO == "15h25":
    print("Você consegue ver o eclipse TOTAL!")
elif HORÁRIO > "15H20" and HORÁRIO > "13h30":
    if ESTADO == "RIO DE JANEIRO" or ESTADO == "SÃO PAULO" or ESTADO == "MINAS GERAIS" or ESTADO == "ESPIRITO SANTO":
        if CONDIÇÕES == "dia claro":
            print("Você só consegue ver o eclipse parcial")
else:
    print("Você não consegue ver o eclipse")