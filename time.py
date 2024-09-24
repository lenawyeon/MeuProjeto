#Time e sua posição. . .
print("Digite seu time:")
TIME = input()
print("Digite sua posição:")
POSIÇÃO = int(input())

if POSIÇÃO == 1:
    print("Campeão!")
elif 2 <= POSIÇÃO <= 6:
    print("Libertadores!")
elif POSIÇÃO >= 7 or POSIÇÃO <= 12:
    print("Sul-Americana!")
elif POSIÇÃO == 13 or POSIÇÃO == 14 or POSIÇÃO == 15 or POSIÇÃO == 16:
    print("Rebaixado!")
