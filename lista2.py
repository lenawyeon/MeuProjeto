#Demonstração de acesso a listas. . . 
print("Vou montar a marmita com 5 alimentos")
MARMITA = ["Feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, aqui a nossa recomendação:", MARMITA)

RESPOSTA = input("Quer montar sua marmita diferente?")
if RESPOSTA == "sim":
    for X in range(len(MARMITA)):
        print(f"Digite o {X + 1}. item do cardápio:")
        MARMITA[X] = input()
    print("A marmita montada foi:", MARMITA)
    print("Os três primeiros itens foram:", MARMITA[0:3])
    print("O último item da marmita foi:", MARMITA[-1])
else:
    print("OK")
