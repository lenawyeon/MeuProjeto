#Demonstração do comportamento das listas. . . 
print("Vou almoçar em um restaurante a quilo.")

ORIGINAL = ["arroz", "feijão", "batata", "alface", "frango"]
print("Eis a minha comida", ORIGINAL)
DERIVADA = ORIGINAL[:]
print("Meu amigo irá comer também:", DERIVADA)

print("Vou alterar as opções sem ele ver. . .")
ORIGINAL.remove("feijão")
ORIGINAL.remove("frango")
ORIGINAL.remove("alface")
ORIGINAL.append("picanha")
ORIGINAL.append("molho_acompanha")

print("Amiginho, me mostre o que você vai comer. . .")
print("Claro!", DERIVADA)
