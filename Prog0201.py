# Escalação de jogadores...
JOGADORES = []
NUMEROS = []

for X in range(0,11):
    NOME = input(f"Digite o nome do jogador:")
    JOGADORES.append(NOME)
    CAMISA = input("Digite o número da camisa:")
    NUMEROS.append(CAMISA)

TROCA = input("Você que fazer substituições") 
if TROCA == "S":
   for X in range(0, 3):
    NOME = input("Digite o nome do jogador substituido") 
    CAMISA = input("Digite o seu respectivo número: ") 
    JOGADORES.remove(NOME)
    NUMEROS.remove(CAMISA)
    NOME = input("Digite i nome do jogador substituto: ")
    CAMISA = input("Digite o seu respectivo número: ")
    JOGADORES.append(NOME)
    NUMEROS.append(CAMISA)

print("Lista dos jogadores Atualiza")
for Y in range(0, 11):
    print(f"{NUMEROS[Y]}. {JOGADORES[Y]}")
       
        