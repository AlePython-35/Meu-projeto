# Demonstraçao de time...
TIME = input("Digite seu time")  
POSIÇÃO = int(input("Digite sua posição"))

if POSIÇÃO == 1:
    print("Campeão!") 
elif POSIÇÃO == 2 or POSIÇÃO == 3 or POSIÇÃO == 4 or POSIÇÃO == 5 or POSIÇÃO == 6:
    print("Libertadores!")
elif POSIÇÃO == 7 or POSIÇÃO == 8 or POSIÇÃO == 9 or POSIÇÃO == 10 or POSIÇÃO == 11 or POSIÇÃO == 12:
    print("Sul-Americana!") 
elif POSIÇÃO == 13 or POSIÇÃO == 14 or POSIÇÃO == 15 or POSIÇÃO == 16:
    print("Rebaixado!")
else:
    print("Não sei dizer...")

