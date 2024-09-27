#Conversão de temperaturas. . .
print("Digite qual temperatura você quer fazer a conversão:")
VALOR = int(input())
print("Digite qual a unidade de medida da sua temperatura:")
UNIDADE1 = input()
print("Digite para qual unidade de medida quer converter:")
UNIDADE2 = input()

if UNIDADE1 == "celsius" and UNIDADE2 == "kelvin":
    K = VALOR + 273 
    print("Resultado =", K)
elif UNIDADE1 == "celsius" and UNIDADE2 == "fahrenheit":
    F = (9 * (VALOR / 5)) + 32
    print("Resultado =", F)
elif UNIDADE1 == "kelvin" and UNIDADE2 == "celsius":
    C = VALOR - 273
    print("Resultado =", C)
elif UNIDADE1 == "kelvin" and UNIDADE2 == "fahrenheit":
    F = (9 * (VALOR - 273) / 5) + 32 
    print("Resultado =", F)
elif UNIDADE1 == "fahrenheit" and UNIDADE2 == "kelvin":
    K = (5 * ((VALOR - 32) / 9)) + 273
    PRINT("Resultado =", K)
elif UNIDADE1 == "fahrenheit" and UNIDADE2 == "celsius":
    C = 5 * ((VALOR - 32) / 9)
    print("Resultado =", C)

                                                                                                                                                              