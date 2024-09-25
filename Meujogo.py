# Programa de lógica..
JOGADOR1 = input("Jogador 1:")
JOGADOR2 = input("Jogador 2:")

if JOGADOR1 == JOGADOR2:
    print("O resultado deu empate!")
elif JOGADOR1 == "tesoura" and JOGADOR2 == "papel":
    print("Jogador 1 venceu!") 
elif JOGADOR1 == "papel" and JOGADOR2 == "pedra":
    print("Jogador 1 venceu!")   
elif JOGADOR1 == "pedra" and JOGADOR2 == "tesoura":
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!')")            
