# Demonstração do uso de for/ range. . . 
print("Digite o valor máximo desejado:")
NÚMERO = int(input())

print("Segue, os números desejados:")
for X in range(0, NÚMERO):
    print(X)
    
print("Digite o nome desejado:")
NOME = input()

print("Vamos soletrar cada letra?")
for X in NOME:
    print(X)