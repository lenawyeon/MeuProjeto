#Demonstração de uso de diferentes operadores. . .
print("Qual é o saldo atual da sua conta bancária?")
print("Obs.: utilize ponto para representar os centavos. . .")
SALDO = float(input())

if SALDO < 0:
    print("Puts! Você está devendo ao banco!")
elif SALDO == 0:
    print("Impossivél! Deve ter alguns centavos aí. . .")
elif SALDO < 1:
    print("Puts! Só miseros centavinhos na conta?")
elif SALDO <= 9:
    print("Opa! Já dá para comprar umas balinhas. . .")
elif SALDO >= 1000000:
    print("Eita! Você tem mais de um milhão!")
if SALDO != 0:
    print("Ao menos, você está movimentando a conta. . .")
