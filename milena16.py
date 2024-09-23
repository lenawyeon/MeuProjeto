#Programa 2. . .
DIA = input("Digite um dia da semana em capslock:")


match DIA:
    case "SEGUNDAFEIRA":
        print("Você pode ir a praia")
    case "TERÇAFEIRA":
        print("Você pode ir a academia")
    case "QUARTAFEIRA":
        print("Você pode ir a feira")
    case "QUINTAFEIRA":
        print("Você pode fazer uma comida diferente")
    case "SEXTAFEIRA":
        print("Você pode estudar sua matéria favorita")
    case "SÁBADO":
        print("Você pode fazer faxina")
    case "DOMINGO":
        print("Hoje você pode descansar")
    case "":
        print("ALERTA")
