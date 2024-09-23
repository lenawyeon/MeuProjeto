#Demonstração do uso da condicional IF/ELIF/ELSE. . .
print("Digite o número referente ao estado da moeda:")
print("1.Flor de cunho")
print("2.Soberba")
print("3.Muito bem conservada")
print("4.Bem conservada")
print("5.Outros estados")
ESTADO = int(input())

if ESTADO == 1:
    print("Perfeita! Vou pagar R$ 1.000.000,00")
elif ESTADO == 2:
    print("Quase perfeita! Ofereço R$ 250.00,00")
elif ESTADO == 3:
    print("Que ótimo! Posso dar uns R$ 100.00,00")
